from ChomChat.Outputer import Outputer, Component
from ChomChat.Outputer.Decorator import RegisterOutputerWithoutQueue
from providers.line.config import *
import requests


@RegisterOutputerWithoutQueue("line")
def output_without_queue(outputer: Outputer, message: Component):
    response = requests.post("https://api.line.me/v2/bot/message/push", headers={
        "Authorization": "Bearer " + CHANNEL_ACCESS_TOKEN
    }, json={
        "to": outputer.context.user.id,
        "messages": [message.format('line')],
    })

    if response.status_code < 200 or response.status_code >= 300:
        raise Exception("[LINE] Push message error (Status: " + str(response.status_code) + "\n" + str(response.text))