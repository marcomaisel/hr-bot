from rasa_core.agent import Agent
from rasa_core.channels.socketio import SocketIOInput
from rasa_core.tracker_store import MongoTrackerStore
from rasa_core.domain import TemplateDomain
from rasa_core.interpreter import (
    NaturalLanguageInterpreter, RasaNLUInterpreter)
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.fallback import FallbackPolicy
import os
import sys

_domain = TemplateDomain.load(os.path.join("models/dialogue", "domain.yml"))

_fallback = FallbackPolicy(fallback_action_name="action_default_fallback",
                           core_threshold=0.3,
                           nlu_threshold=0.3)

_interpreter = RasaNLUInterpreter("models/current/nlu/")

_tracker_store = MongoTrackerStore(_domain,
                                   host="mongodb://localhost:27017",
                                   db="rasa",
                                   username=None,
                                   password=None,
                                   collection="conversations")

agent = Agent(policies=[MemoizationPolicy(), KerasPolicy(), _fallback])

agent = Agent.load("models/dialogue",
                   interpreter=_interpreter,
                   tracker_store=_tracker_store)

agent.handle_channels([SocketIOInput()], 5500, serve_forever=True)
