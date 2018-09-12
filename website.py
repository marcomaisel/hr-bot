from rasa_addons.webchat import WebChatInput, SocketInputChannel
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
import os
import sys

#interpreter = RasaNLUInterpreter("models/current/nlu/")
agent = Agent.load("models/dialogue/", "models/current/nlu/")

input_channel = WebChatInput(static_assets_path=os.path.join(
    os.path.dirname(os.path.realpath(__file__)), 'index.html'))
agent.handle_channels(SocketInputChannel(5500, "/bot", input_channel))
