from ChomChat.Decorator import RegisterContextBuilder
from ChomChat import User
from providers.line.request_model import LineRequestEvent, LineUser
from providers.line.config import *

import requests


def build_user(raw: LineRequestEvent):
    response = requests.get("https://api.line.me/v2/bot/profile/" + raw.source.userId, headers={
        "Authorization": "Bearer "+CHANNEL_ACCESS_TOKEN
    })

    if response.status_code < 200 or response.status_code >= 300:
        raise Exception("[LINE] Get user profile error (Status: "+str(response.status_code)+"\n"+str(response.text))

    user_data = response.json()
    user_data = LineUser(**user_data)
    raw.user = user_data

    return User("line", raw.source.userId, user_data.displayName, raw, user_data.pictureUrl)


@RegisterContextBuilder("line")
def context_builder(raw: LineRequestEvent):
    return build_user(raw).context
