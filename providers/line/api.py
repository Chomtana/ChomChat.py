from fastapi import FastAPI, Request, Body
from app import app
from providers.line.request_model import LineRequest
from providers.line.context_builder import *
from providers.line.context_getter import *


@app.post("/chomchat/line")
async def line(body: LineRequest):
    for raw in body.events:
        raw.destination = body.destination
        context = context_getter(raw)
        if raw.message['type'] == 'text':
            context.perform_on_message(raw.message['text'])
    return body