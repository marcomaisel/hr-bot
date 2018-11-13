from rasa_core_sdk import Action
from rasa_core_sdk.events import *
from job_db_actions import get_task_for_technology, get_task_for_domain, get_domain_for_task, get_domain_for_technology, get_technology_for_domain, get_technology_for_task, get_domain_for_task_and_tech, get_task_for_domain_and_tech, get_technology_for_task_and_domain

jobs = [
    {"name": "Werkstudent Software-Entwicklung", "formOfEmployment": "werkstudent",
        "jobTask": ["entwickeln"], "domain": ["web", "mobile"], "technology": ["java ee", "java"]},

    {"name": "Webdesigner", "formOfEmployment": "vollzeit", "jobTask": [
        "designen"], "domain": ["web"], "technology": ["photoshop", "html", "css", "javascript"]},

    {"name": "Praktikant Webdesign", "formOfEmployment": "praktikum",
        "jobTask": "[designen]", "domain": ["web"], "technology": "photoshop"},

    {"name": "Frontend Developer", "formOfEmployment": "vollzeit", "jobTask": ["entwickeln", "designen"], "domain": ["web", "mobile", "frontend"], "technology": [
        "angular", "typescript", "javascript", "html", "css", "sass", "less", "react", "vue", "jquery", "npm", "buildtools", "photoshop", "illustrator", "sketch", "invision", "ui-test"]}

]


class ActionFindExistingJob(Action):

    def name(self):
        # type: () -> Text
        return "action_find_job"

    def run(self, dispatcher, tracker, domain):
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
            domain = job["domain"]
            employment = job["formOfEmployment"]

            # Search for matches between slots sent by the user and stored jobs in the jobs list.
            # If a job has at least one value for each key in the dictionary the job is appended to the foundJobs list.
            if [i.lower() for i in technologySlot if i.lower() in tech] and \
                [i.lower() for i in domainSlot if i.lower() in domain] and \
                [i.lower() for i in taskSlot if i.lower() in task] and \
                    [i.lower() for i in formOfEmploymentSlot if i.lower() in employment]:
                foundJobs.append(job)

        # Create a message for the user with a list of names of all found jobs, separated by comma
        jobMessage = ", ".join([c["name"] for c in foundJobs])

        print("JobMessage: " + jobMessage)
        # Send message with all found jobs to the user with the dispatcher object
        dispatcher.utter_message("{}".format(jobMessage))

        # Set jobs slot with all found jobs
        return [SlotSet("jobs", foundJobs if foundJobs is not None else [])]


class ActionShowTechnologies(Action):

    def name(self):
        # type: () -> Text
        return "action_show_technologies"

    def run(self, dispatcher, tracker, domain):

        # Store the values of slots given by the user with the tracker object
        possibleTechnologySlot = tracker.get_slot('possibleTechnologies')

        # Send message to user with the dispatcher object
        dispatcher.utter_message(
            "Mögliche Technologien sind z.B.: " + list[:6] + ".")

        return [FollowupAction("utter_askTechnology")]


class ActionMatchJobSlots(Action):
    def name(self):
        # type: () -> Text
        return "action_match_job_slots"

    def run(self, dispatcher, tracker, domain):
        foundJobsByName = []

        # Store the values of slots given by the user with the tracker object
        taskSlot = tracker.get_slot('jobTask')
        domainSlot = tracker.get_slot('domain')
        technologySlot = tracker.get_slot('technology')
        latest_message = (tracker.latest_message)['text']

    # search for jobName in latest user utterance
        for job in jobs:
            # Store the name for all job dictionaries in the jobs list
            jobName = job["name"]

            if(jobName in latest_message):
                foundJobsByName.append(job)

        if len(foundJobsByName) >= 1:
            jobMessage = ", ".join([c["name"] for c in foundJobsByName])

            # Send message with all found jobs to the user with the dispatcher object
            dispatcher.utter_message(
                "Ich habe folgende Jobs für dich gefunden:")
            dispatcher.utter_message("{}".format(jobMessage))

            # Set jobs slot with all found jobs
            return [SlotSet("jobs", foundJobsByName if foundJobsByName is not None else []), FollowupAction("action_listen")]

    # if no job could be found in the users utterance proceed with questions
        else:
            # for given task and domain: ask for technologies
            if taskSlot is not None and domainSlot is not None:

                possibleTechnologies = get_technology_for_task_and_domain(
                    taskSlot, domainSlot)

                return [
                    SlotSet("possibleTechnologies", possibleTechnologies),
                    FollowupAction("utter_askTechnology")]

            # for given task and technology: differentiate between 1 or more than 1 possible domain
            elif taskSlot is not None and technologySlot is not None:

                possibleDomains = get_domain_for_task_and_tech(
                    taskSlot, technologySlot)

                # if only 1 domain is possible: automatically set it and proceed with action_find_job
                if len(possibleDomains) == 1:
                    return [
                        SlotSet("domain", possibleDomains),
                        FollowupAction("action_find_job")]

                # if no domain is possible:
                elif len(possibleDomains) == 0:
                    return [FollowupAction("utter_askSpeculativeApplication")]

                # if more than 1 domain is possible: ask for domain
                else:

                    message = "Für welches dieser Gebiete interessiert du dich am meisten?"
                    buttons = []
                    for possDomain in possibleDomains:
                        payload = (
                            '/enter_data{\"domain\":' + '\"' + possDomain + '\"}')
                        buttons.append(
                            {"title": possDomain, "payload": payload})
                    dispatcher.utter_button_message(message, buttons)

                    return [
                        SlotSet("possibleDomains", possibleDomains)]

            # for given domain and technology: differentiate between 1 or more than 1 possible task
            elif domainSlot is not None and technologySlot is not None:

                possibleTasks = get_task_for_domain_and_tech(
                    domainSlot, technologySlot)

                # if only 1 task is possible: automatically set it and proceed with action_find_job
                if len(possibleTasks) == 1:
                    return [
                        SlotSet("jobTask", possibleTasks),
                        FollowupAction("action_find_job")]

                # if no task is possible:
                elif len(possibleTasks) == 0:
                    return [FollowupAction("utter_askSpeculativeApplication")]

                # if more than 1 task is possible: ask for task
                else:
                    message = "Welche dieser Tätigkeiten beschreibt deine gesucht Stelle am besten?"
                    buttons = []
                    for possTask in possibleTasks:
                        payload = (
                            '/enter_data{\"jobTask\":' + '\"' + possTask + '\"}')
                        buttons.append({"title": possTask, "payload": payload})
                    dispatcher.utter_button_message(message, buttons)

                    return [
                        SlotSet("possibleTasks", possibleTasks),
                        FollowupAction("action_listen")]

            elif taskSlot is not None:

                possibleDomains = get_domain_for_task(taskSlot)
                possibleTechnologies = get_technology_for_task(taskSlot)

                # if only 1 domain is possible: automatically set it and ask for technology
                if len(possibleDomains) == 1:
                    return[
                        SlotSet("possibleTechnologies", possibleTechnologies),
                        SlotSet("domain", possibleDomains),
                        FollowupAction("utter_askTechnology")]

                # if no domain is possible:
                elif len(possibleDomains) == 0:
                    return [FollowupAction("utter_askSpeculativeApplication")]

                # if more than 1 domain is possible: ask for technology
                else:
                    return [
                        SlotSet("possibleTechnologies", possibleTechnologies),
                        SlotSet("possibleDomains", possibleDomains),
                        FollowupAction("utter_askTechnology")]

            elif domainSlot is not None:

                possibleTasks = get_task_for_domain(domainSlot)
                possibleTechnologies = get_technology_for_domain(domainSlot)

                # if only 1 task is possible: automatically set it and ask for technology
                if len(possibleTasks) == 1:
                    return[
                        SlotSet("possibleTechnologies", possibleTechnologies),
                        SlotSet("jobTask", possibleTasks),
                        FollowupAction("utter_askTechnology")]

                # if no task is possible:
                elif len(possibleTasks) == 0:
                    return [FollowupAction("utter_askSpeculativeApplication")]

                # if more than 1 task is possible: ask for domain
                else:
                    return [
                        SlotSet("possibleTechnologies", possibleTechnologies),
                        SlotSet("possibleTasks", possibleTasks),
                        FollowupAction("utter_askTechnology")]

            elif technologySlot is not None:
                possibleDomains = get_domain_for_technology(technologySlot)
                possibleTasks = get_task_for_technology(technologySlot)

                # if only 1 task is possible and only 1 domain is possible:
                # automatically set both and proceed with action_find_job
                if len(possibleTasks) == 1 and len(possibleDomains) == 1:
                    return [
                        SlotSet("jobTask", possibleTasks),
                        SlotSet("domain", possibleDomains),
                        FollowupAction("action_find_job")]

                # if only 1 task is possible: automatically set it
                # ask for domain in form of buttons of all domains which are still possible
                elif len(possibleTasks) == 1:

                    message = "Für welches dieser Gebiete interessiert du dich am meisten?"
                    buttons = []
                    for possDomain in possibleDomains:
                        payload = (
                            '/enter_data{\"domain\":' + '\"' + possDomain + '\"}')
                        buttons.append(
                            {"title": possDomain, "payload": payload})
                    dispatcher.utter_button_message(message, buttons)

                    return [
                        SlotSet("jobTask", possibleTasks),
                        SlotSet("possibleDomains", possibleDomains),
                        FollowupAction("action_listen")]

                # if only 1 domain is possible: automatically set it
                # ask for task in form of buttons of all tasks which are still possible
                elif len(possibleDomains) == 1:

                    message = "Welche dieser Tätigkeiten beschreibt deine gesucht Stelle am besten?"
                    buttons = []
                    for possTask in possibleTasks:
                        payload = (
                            '/enter_data{\"jobTask\":' + '\"' + possTask + '\"}')
                        buttons.append({"title": possTask, "payload": payload})
                    dispatcher.utter_button_message(message, buttons)

                    return [
                        SlotSet("possibleTasks", possibleTasks),
                        SlotSet("domain", possibleDomains),
                        FollowupAction("action_listen")]

                # if no task is possible:
                elif ((len(possibleTasks) == 0) or (len(possibleDomains) == 0)):
                    return [FollowupAction("utter_askSpeculativeApplication")]

                # if non or more than 1 in both slots is possible:
                # ask for domain in form of buttons of all domains which are still possible
                else:
                    message = "Für welches dieser Gebiete interessiert du dich am meisten?"
                    buttons = []
                    for possDomain in possibleDomains:
                        payload = (
                            '/enter_data{\"domain\":' + '\"' + possDomain + '\"}')
                        buttons.append(
                            {"title": possDomain, "payload": payload})
                    dispatcher.utter_button_message(message, buttons)

                    return [
                        SlotSet("possibleTasks", possibleTasks),
                        SlotSet("possibleDomains", possibleDomains),
                        FollowupAction("action_listen")]
            return
