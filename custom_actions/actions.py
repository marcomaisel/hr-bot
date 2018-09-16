from rasa_core_sdk import Action
from rasa_core_sdk.events import *
from job_db_actions import get_task_for_technology, get_task_for_domain, get_domain_for_task, get_domain_for_technology, get_technology_for_domain, get_technology_for_task, get_domain_for_task_and_tech, get_task_for_domain_and_tech, get_technology_for_task_and_domain


class ActionFindExistingJob(Action):
    def name(self):
        # type: () -> Text
        return "action_find_job"

    def run(self, dispatcher, tracker, domain):
        jobs = [
            {"name": "Werkstudent Software-Entwicklung", "formOfEmployment": "student",
             "jobTask": "entwicklung", "domain": ["web", "mobile"], "technology": ["java ee", "java"]},

            {"name": "Webdesigner", "formOfEmployment": "vollzeit", "jobTask": "design",
             "domain": ["web"], "technology": ["photoshop", "html", "css", "javascript"]},

            {"name": "Praktikant Webdesign", "formOfEmployment": "praktikum", "jobTask": "design",
             "domain": ["web"], "technology": "photoshop"}
        ]

        foundJobs = []

        # Store the values of slots given by the user with the tracker object
        taskSlot = tracker.get_slot('jobTask')
        domainSlot = tracker.get_slot('domain')
        technologySlot = tracker.get_slot('technology')
        formOfEmploymentSlot = tracker.get_slot('formOfEmployment')

        # Send message to user with the dispatcher object
        dispatcher.utter_message(
            "Ich habe folgende Stellenanzeigen für dich gefunden:")

        for job in jobs:
            # Store the values of each key for all job dictionaries in the jobs list
            tech = job["technology"]
            task = job["jobTask"]
            metatech = job["domain"]
            employment = job["formOfEmployment"]

            # Search for matches between slots sent by the user and stored jobs in the jobs list.
            # If a job has at least one value for each key in the dictionary the job is appended to the foundJobs list.
            if [i for i in technologySlot if i in tech] and \
               [i for i in domainSlot if i in metatech] and \
               taskSlot in task and \
               formOfEmploymentSlot in employment:
                foundJobs.append(job)

        # Create a message for the user with a list of names of all found jobs, separated by comma
        jobMessage = ", ".join([c["name"] for c in foundJobs])

        # Send message with all found jobs to the user with the dispatcher object
        dispatcher.utter_message("{}".format(jobMessage))

        # Set jobs slot with all found jobs
        return [SlotSet("jobs", foundJobs if foundJobs is not None else [])]


class ActionMatchJobSlots(Action):
    def name(self):
        # type: () -> Text
        return "action_match_job_slots"

    def run(self, dispatcher, tracker, domain):

        # Store the values of slots given by the user with the tracker object
        taskSlot = tracker.get_slot('jobTask')
        domainSlot = tracker.get_slot('domain')
        technologySlot = tracker.get_slot('technology')
        # possibleTaskSlot = tracker.get_slot('possibleTasks')
        # possibleTechnologySlot = tracker.get_slot('possibleTechnologies')
        # possibleDomainSlot = tracker.get_slot('possibleDomains')

        # for given task and domain: ask for technologies
        if taskSlot is not None and domainSlot is not None:

            possibleTechnologies = get_technology_for_task_and_domain(
                taskSlot, domainSlot)

            return [
                SlotSet("possibleTechnologies", possibleTechnologies),
                FollowupAction("utter_askTechnology")]

        # for given task and technology differentiate between 1 or more than 1 possible domain
        elif taskSlot is not None and technologySlot is not None:

            possibleDomains = get_domain_for_task_and_tech(
                taskSlot, technologySlot)

            # if only 1 domain is possible automatically set it and proceed with action_find_job
            if len(possibleDomains) < 2:
                return [
                    SlotSet("domain", possibleDomains),
                    FollowupAction("action_find_job")]

            # if more than 1 domain is possible: ask for domain
            else:
                return [
                    SlotSet("possibleDomains", possibleDomains),
                    FollowupAction("utter_askDomain")]

        # for given domain and technology: present a list of all possible tasks to choose from
        elif domainSlot is not None and technologySlot is not None:

            possibleTasks = get_task_for_domain_and_tech(
                domainSlot, technologySlot)

            # if only 1 task is possible automatically set it and proceed with action_find_job
            if len(possibleTasks) < 2:
                return [
                    SlotSet("jobTask", possibleTasks),
                    FollowupAction("action_find_job")]

            # if more than 1 task is possible: ask for task
            else:
                return [
                    SlotSet("possibleTasks", possibleTasks),
                    FollowupAction("utter_askTask")]

        elif taskSlot is not None:

            possibleDomains = get_domain_for_task(taskSlot)
            possibleTechnologies = get_technology_for_task(taskSlot)

            # if only 1 domain is possible automatically set it
            if len(possibleDomains) < 2:
                SlotSet("domain", possibleDomains)

            return [
                SlotSet("possibleTechnologies", possibleTechnologies),
                SlotSet("possibleDomains", possibleDomains),
                FollowupAction("utter_askTechnology")]

        elif domainSlot is not None:

            possibleTasks = get_task_for_domain(domainSlot)
            possibleTechnologies = get_technology_for_domain(domainSlot)

            # if only 1 task is possible automatically set it
            if len(possibleTasks) < 2:
                SlotSet("jobTask", possibleTasks)

            return [
                SlotSet("possibleTechnologies", possibleTechnologies),
                SlotSet("possibleTasks", possibleTasks),
                FollowupAction("utter_askTechnology")]

        elif technologySlot is not None:
            possibleDomains = get_domain_for_technology(technologySlot)
            possibleTasks = get_task_for_technology(technologySlot)

            # if only 1 task is possible and only 1 domain is possible automatically set both
            if len(possibleTasks) < 2 and len(possibleDomains) < 2:
                return [
                    SlotSet("jobTask", possibleTasks),
                    SlotSet("domain", possibleDomains),
                    FollowupAction("action_find_job")]

            # if only 1 task is possible automatically set it
            elif len(possibleTasks) < 2:
                print("possibleTasks: ", possibleTasks)
                return [
                    SlotSet("jobTask", possibleTasks),
                    SlotSet("possibleDomains", possibleDomains),
                    FollowupAction("utter_askDomain")]

            # if only 1 domain is possible automatically set it
            elif len(possibleDomains) < 2:
                return [
                    SlotSet("possibleTasks", possibleTasks),
                    SlotSet("domain", possibleDomains),
                    FollowupAction("utter_askTask")]

            else:
                return [
                    SlotSet("possibleTasks", possibleTasks),
                    SlotSet("possibleDomains", possibleDomains),
                    FollowupAction("utter_askTask")]

            # for job in jobs:
            #     # Store the values of each key for all job dictionaries in the jobs list
            #     tech = job["technology"]
            #     task = job["jobTask"]
            #     metatech = job["domain"]
            #     employment = job["formOfEmployment"]

            #     # Search for matches between slots sent by the user and stored jobs in the jobs list.
            #     # If a job has at least one value for each key in the dictionary the job is appended to the foundJobs list.
            #     if [i for i in technologySlot if i in tech] and \
            #        [i for i in domainSlot if i in metatech] and \
            #        taskSlot in task and \
            #        formOfEmploymentSlot in employment:
            #         foundJobs.append(job)

            # # Create a message for the user with a list of names of all found jobs, separated by comma
            # jobMessage = ", ".join([c["name"] for c in foundJobs])

            # # Send message with all found jobs to the user with the dispatcher object
            # dispatcher.utter_message("{}".format(jobMessage))

            # Set jobs slot with all found jobs
            # return [SlotSet("jobs", foundJobs if foundJobs is not None else [])]
        return