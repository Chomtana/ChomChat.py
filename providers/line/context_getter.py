from ChomChat.ChomChat import global_chom_chat
from ChomChat.Decorator import RegisterContextGetter
from providers.line.request_model import LineRequestEvent


@RegisterContextGetter("line")
def context_getter(raw: LineRequestEvent):
    user_id = raw.source.userId
    return global_chom_chat.get_context("line", user_id, raw)