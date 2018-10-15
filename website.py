from rasa_core.agent import Agent
from rasa_core.channels.socketio import SocketIOInput
from rasa_core.tracker_store import MongoTrackerStore
from rasa_core.domain import TemplateDomain
from rasa_core.interpreter import (
    NaturalLanguageInterpreter)
import os
import sys

domain = TemplateDomain.load(os.path.join("models/dialogue", "domain.yml"))

# fallback = FallbackPolicy(fallback_action_name="action_default_fallback",
#                           core_threshold=0.3,
#                           nlu_threshold=0.3)

tracker_store = MongoTrackerStore(domain,
                                  host="mongodb://localhost:27017",
                                  db="rasa",
                                  username=None,
                                  password=None,
                                  collection="conversations")

agent = Agent.load("models/dialogue/", "models/current/nlu/",
                   tracker_store=tracker_store)

agent.handle_channels([SocketIOInput()], 5500, serve_forever=True)
