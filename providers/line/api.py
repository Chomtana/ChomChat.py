from fastapi import FastAPI, Request, Body
from app import app
from providers.line.request_model import LineRequest

# Init context
from providers.line.context_builder import *
from providers.line.context_getter import *

# Init outputer
from providers.line.output_without_queue import *
from providers.line.output_with_queue import *


@app.post("/chomchat/line")
async def line(body: LineRequest):
    if body.destination is None: return body

    for raw in body.events:
        raw.destination = body.destination
        context = context_getter(raw)
        if raw.message['type'] == 'text':
            context.outputer.start_session({
                'replyToken': raw.replyToken
            })
            context.perform_on_message(raw.message['text'])
            context.outputer.commit()
    return body
