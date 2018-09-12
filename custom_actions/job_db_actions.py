from pony.orm import *

db = Database()
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)


class Task(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    technologies = Set('Technology')
    domains = Set('Domain')


class Technology(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    tasks = Set('Task')
    domains = Set('Domain')


class Domain(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    tasks = Set(Task)
    technologies = Set('Technology')
    otherDomains = Set('Domain', reverse='otherDomains')


db.generate_mapping(create_tables=True)


result = select(p for p in Technology)


# Get Tasks for Technology
@db_session
def get_task_for_technology(inTech):

    if inTech is not None:
        inTech = inTech.lower()
        result = select(tech for tech in Technology if tech.name == inTech)[:]
        for tech in result:
            taskName = []
            for task in tech.tasks:
                taskName.append(task.name)
            print("TaskForTech: ", taskName)
            return taskName

    else:
        return []


# Get Domains for Technology
@db_session
def get_domain_for_technology(inTech):

    if inTech is not None:
        inTech = inTech.lower()
        result = select(tech for tech in Technology if tech.name == inTech)[:]
        for tech in result:
            domainName = []
            for domain in tech.domains:
                domainName.append(domain.name)
            print("DomainForTech: ", domainName)
            return domainName

    else:
        return []


# Get Technology for Task
@db_session
def get_technology_for_task(inTask):

    if inTask is not None:
        inTask = inTask.lower()
        result = select(task for task in Task if task.name == inTask)[:]
        for task in result:
            technologyName = []
            for technology in task.technologies:
                technologyName.append(technology.name)
            print("TechnologyForTask: ", technologyName)
            return technologyName

    else:
        return []


# Get Domain for Task
@db_session
def get_domain_for_task(inTask):

    if inTask is not None:
        inTask = inTask.lower()
        result = select(task for task in Task if task.name == inTask)[:]
        for task in result:
            domainName = []
            for domain in task.domains:
                domainName.append(domain.name)
            print("DomainForTask: ", domainName)
            return domainName

    else:
        return []


# Get Technology for Domain
@db_session
def get_technology_for_domain(inDomain):

    if inDomain is not None:
        inDomain = inDomain.lower()
        result = select(
            domain for domain in Domain if domain.name == inDomain)[:]
        for domain in result:
            technologyName = []
            for technology in domain.technologies:
                technologyName.append(technology.name)
            print("TechnologyForDomain: ", technologyName)
            return technologyName

    else:
        return []


# Get Task for Domain
@db_session
def get_task_for_domain(inDomain):

    if inDomain is not None:
        inDomain = inDomain.lower()
        result = select(
            domain for domain in Domain if domain.name == inDomain)[:]
        for domain in result:
            taskName = []
            for task in domain.tasks:
                taskName.append(task.name)
            print("TaskForDomain: ", taskName)
            return taskName

    else:
        return []


# Get Task for Domain and Technology
@db_session
def get_task_for_domain_and_tech(inDomain, inTech):

    if inDomain is not None and inTech is not None:
        taskNameinDomain = get_task_for_domain(inDomain)
        taskNameinTech = get_task_for_technology(inTech)

        if taskNameinDomain is not None and taskNameinTech is not None:
            tasksInCommon = list(
                set(taskNameinDomain).intersection(taskNameinTech))
            print(tasksInCommon)
            return tasksInCommon
        else:
            return []

    else:
        return []


# Get Domain for Task and Technology
@db_session
def get_domain_for_task_and_tech(inTask, inTech):

    if inTask is not None and inTech is not None:
        domainNameinTask = get_domain_for_task(inTask)
        domainNameinTech = get_domain_for_technology(inTech)

        if domainNameinTask is not None and domainNameinTech is not None:
            domainsInCommon = list(
                set(domainNameinTask).intersection(domainNameinTech))
            print(domainsInCommon)
            return domainsInCommon
        else:
            return []

    else:
        return []


# Get Technology for Task and Domain
@db_session
def get_technology_for_task_and_domain(inTask, inDomain):

    if inTask is not None and inDomain is not None:
        techNameinTask = get_technology_for_task(inTask)
        techNameinDomain = get_technology_for_domain(inDomain)

        if techNameinTask is not None and techNameinDomain is not None:
            techsInCommon = list(
                set(techNameinTask).intersection(techNameinDomain))
            print(techsInCommon)
            return techsInCommon
        else:
            return []

    else:
        return []


# Populate Database
@db_session
def populate_database():

    # Tasks
    entwicklung = Task(name='entwicklung')
    design = Task(name='design')

    # Domains
    web = Domain(name="web", tasks=[entwicklung, design], otherDomains=[])
    mobile = Domain(name="mobile", tasks=[
                    entwicklung, design], otherDomains=[])
    backend = Domain(name="backend", tasks=[entwicklung], otherDomains=[])
    devops = Domain(name="devops", tasks=[entwicklung], otherDomains=[])
    frontend = Domain(name="frontend", tasks=[
                      entwicklung], otherDomains=[web, mobile])
    fullstack = Domain(name="fullstack", tasks=[entwicklung], otherDomains=[
                       web, mobile, backend, frontend])

    # Technologies
    angular = Technology(name='angular', tasks=[
                         entwicklung], domains=[frontend, web, fullstack])
    java = Technology(name='java', tasks=[entwicklung], domains=[
                      frontend, backend, fullstack, mobile, web])
    kotlin = Technology(name='kotlin', tasks=[entwicklung], domains=[
                        backend, fullstack, mobile])
    swift = Technology(name='swift', tasks=[entwicklung], domains=[
                       backend, fullstack, mobile])
    typescript = Technology(name='typescript', tasks=[entwicklung], domains=[
                            frontend, backend, fullstack, mobile, web])
    javascript = Technology(name='javascript', tasks=[entwicklung], domains=[
                            frontend, backend, fullstack, mobile, web])
    c = Technology(name='c', tasks=[entwicklung], domains=[backend, fullstack])
    csharp = frontend, backend, fullstack, mobile, web

    docker = Technology(name='docker', tasks=[entwicklung], domains=[devops])
    openshift = Technology(name='openshift', tasks=[
                           entwicklung], domains=[devops])
    ci = Technology(name='continuous integration', tasks=[
                    entwicklung], domains=[devops])
    cd = Technology(name='continuous deployment', tasks=[
                    entwicklung], domains=[devops])
    commit()


if __name__ == "__main__":
    with db_session:
        if Technology.select().first() is None:
            populate_database()
    # get_domain_for_technology('angular')
    # get_task_for_technology('angular')
    # get_technology_for_task('entwicklung')
    # get_domain_for_task('entwicklung')
    # get_task_for_domain('web')
    # get_technology_for_domain('web')
    # get_task_for_domain_and_tech('web', 'angular')
    # get_domain_for_task_and_tech('entwicklung', 'angular')
    # get_technology_for_task_and_domain('entwicklung', 'web')
