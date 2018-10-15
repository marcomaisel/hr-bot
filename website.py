from rasa_core.agent import Agent
from rasa_core.channels.socketio import SocketIOInput
from rasa_core.tracker_store import MongoTrackerStore
from rasa_core.domain import TemplateDomain
from rasa_core.interpreter import (
    NaturalLanguageInterpreter)
import os
import sys

domain = TemplateDomain.load(os.path.join("models/dialogue", "domain.yml"))

# _interpreter = NaturalLanguageInterpreter.create("models/current/nlu/")

_tracker_store = MongoTrackerStore(domain,
                                   host="mongodb://localhost:27017",
                                   db="rasa",
                                   username=None,
                                   password=None,
                                   collection="conversations")

agent = Agent.load("models/dialogue/", "models/current/nlu/",
                   #    interpreter=_interpreter,
                   tracker_store=_tracker_store)

agent.handle_channels([SocketIOInput()], 5500, serve_forever=True)
