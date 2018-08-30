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
    tasks = Set(Task)
    domains = Set('Domain')


class Domain(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    tasks = Set(Task)
    technologies = Set(Technology)
    otherDomains = Set('Domain', reverse='otherDomains')


db.generate_mapping(create_tables=True)


result = select(p for p in Technology)


@db_session
def get_technology():

    result = select(tech for tech in Technology)[:]
    for tech in result:
        tech1 = tech.name
        for task in tech.tasks:
            task1 = task.name
        for domain in tech.domains:
            domain1 = domain.name
        print(tech1, domain1, task1)


@db_session
def populate_database():
    development = Task(name='Development')
    design = Task(name='Design')
    angular = Technology(name='Angular', tasks=development)
    frontend = Domain(name="Frontend", tasks=development)
    # web = Domain(name="Web", task=development)
    commit()

# @db_session
# def add_technology(name, tasks, domains):
#     Technology(name=name, tasks=tasks, domains=domains)
#     # commit() will be done automatically
#     # database session cache will be cleared automatically
#     # database connection will be returned to the pool


if __name__ == "__main__":
    with db_session:
        if Technology.select().first() is None:
            populate_database()
    get_technology()
