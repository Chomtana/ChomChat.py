from ChomChat.Decorator import RegisterContextBuilder
from ChomChat import User
from providers.line.build_user import build_user
from providers.line.request_model import LineRequestEvent, LineUser
from providers.line.config import *

import requests


@RegisterContextBuilder("line")
def context_builder(raw: LineRequestEvent):
    return build_user(raw).context
