from rasa_core.agent import Agent
from rasa_core.channels.socketio import SocketIOInput
import os
import sys

agent = Agent.load("models/dialogue/", "models/current/nlu/")

agent.handle_channels([SocketIOInput()], 5500, serve_forever=True)
