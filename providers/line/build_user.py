import requests

from ChomChat import User
from providers.line.config import CHANNEL_ACCESS_TOKEN
from providers.line.request_model import LineRequestEvent, LineUser


def build_user(raw: LineRequestEvent, user: User = None):
    response = requests.get("https://api.line.me/v2/bot/profile/" + raw.source.userId, headers={
        "Authorization": "Bearer "+CHANNEL_ACCESS_TOKEN
    })

    if response.status_code < 200 or response.status_code >= 300:
        raise Exception("[LINE] Get user profile error (Status: "+str(response.status_code)+"\n"+str(response.text))

    user_data = response.json()
    user_data = LineUser(**user_data)
    raw.user = user_data

    if user is None:
        return User("line", raw.source.userId, user_data.displayName, raw, user_data.pictureUrl)
    else:
        user.update("line", raw.source.userId, user_data.displayName, raw, user_data.pictureUrl)
        return user
