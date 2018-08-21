from rasa_core.actions import Action
from rasa_core.events import SlotSet


class ActionFindJob(Action):
    def name(self):
        # type: () -> Text
        return "action_find_job"

    def run(self, dispatcher, tracker, domain):
        jobs = [
            {"name": "Werkstudent Software-Entwicklung", "type": "student"},
            {"name": "DevOps Spezialist", "type": "fulltime"}
        ]
        dispatcher.utter_message("Ich habe folgende Stellenanzeigen gefunden")
        description = ", ".join([c["name"] for c in jobs])
        dispatcher.utter_message("{}".format(description))
        return [SlotSet("jobs", jobs)]
