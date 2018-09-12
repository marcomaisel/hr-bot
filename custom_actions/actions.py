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

        if taskSlot is not None and domainSlot is not None:
            get_technology_for_task_and_domain(taskSlot, domainSlot)
            return [FollowupAction("utter_askTechnology")]

        elif taskSlot is not None and technologySlot is not None:
            get_domain_for_task_and_tech(taskSlot, technologySlot)
            return [FollowupAction("utter_askDomain")]

        elif domainSlot is not None and technologySlot is not None:
            get_task_for_domain_and_tech(domainSlot, technologySlot)
            return [FollowupAction("utter_askTask")]

        elif taskSlot is not None:
            get_domain_for_task(taskSlot)
            get_technology_for_task(taskSlot)

        elif domainSlot is not None:
            get_task_for_domain(domainSlot)
            get_technology_for_domain(domainSlot)

        elif technologySlot is not None:
            get_domain_for_technology(technologySlot)
            get_task_for_technology(technologySlot)

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
