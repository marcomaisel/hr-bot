from rasa_core.agent import Agent
from rasa_core.channels.socketio import SocketIOInput
from rasa_core.tracker_store import MongoTrackerStore
from rasa_core.domain import TemplateDomain
import os
import sys

domain = TemplateDomain.load(os.path.join('./models/dialogue', "domain.yml"))


# tracker_store = MongoTrackerStore(domain, host="mongodb://localhost:27017",
#                                   db="rasa",
#                                   username=None,
#                                   password=None,
#                                   collection="conversations")

# agent = Agent.load("models/dialogue/", "models/current/nlu/", tracker_store)
agent = Agent.load("models/dialogue/", "models/current/nlu/")

agent.handle_channels([SocketIOInput()], 5500, serve_forever=True)
