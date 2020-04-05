from ChomChat.Outputer import OutputerQueue
from ChomChat.Outputer.Decorator import RegisterOutputerWithQueue
from providers.line.output_without_queue import output_without_queue
import warnings
from config import DEBUG_MODE
from providers.line.config import *
import requests


@RegisterOutputerWithQueue("line")
def output_with_queue(queue: OutputerQueue):
    if isinstance(queue.metadata, dict) and 'replyToken' in queue.metadata:
        response = requests.post("https://api.line.me/v2/bot/message/reply", headers={
            "Authorization": "Bearer " + CHANNEL_ACCESS_TOKEN
        }, json={
            "replyToken": queue.metadata['replyToken'],
            "messages": queue.format('line'),
        })

        if response.status_code < 200 or response.status_code >= 300:
            raise Exception("[LINE] Reply error (Status: " + str(response.status_code) + "\n" + str(response.text))
    else:
        if DEBUG_MODE:
            warnings.warn(f"[LINE] Queue {queue.name} does not has replyToken in metadata ... use EXPENSIVE mode")

        response = requests.post("https://api.line.me/v2/bot/message/push", headers={
            "Authorization": "Bearer " + CHANNEL_ACCESS_TOKEN
        }, json={
            "to": queue.outputer.context.user.id,
            "messages": queue.format('line'),
        })

        if response.status_code < 200 or response.status_code >= 300:
            raise Exception(
                "[LINE] Push (multi) message error (Status: " + str(response.status_code) + "\n" + str(response.text))