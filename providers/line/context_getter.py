from ChomChat.ChomChat import global_chom_chat
from ChomChat.Decorator import RegisterContextGetter
from providers.line.build_user import build_user
from providers.line.request_model import LineRequestEvent


@RegisterContextGetter("line")
def context_getter(raw: LineRequestEvent):
    user_id = raw.source.userId
    context = global_chom_chat.get_context("line", user_id, raw)

    if context.user.expired():
        build_user(raw, context.user)

    return context
