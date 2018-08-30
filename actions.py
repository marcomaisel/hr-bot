#!/usr/bin/env python
# coding: utf8

from rasa_core.actions import Action
from rasa_core.events import SlotSet


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
