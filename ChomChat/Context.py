from __future__ import annotations
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from ChomChat import ChomChat, ChatState, StateBase, User

from ChomChat.Outputer import Outputer
from ChomChat.ChomChat import global_chom_chat
from states.RootState import RootState
from ChomChat.Scheduler import Scheduler


class Context:
    chat_states: List[ChatState]
    state: StateBase
    user: User

    outputer: Outputer
    scheduler: Scheduler

    def __init__(self, user: User):
        self.chat_states = []
        self.state = RootState(self)

        user.context = self
        global_chom_chat.contexts[user.id] = self

        self.user = user

        self.outputer = Outputer(self)
        self.scheduler = Scheduler(self)

        self.interrupt('_start')

    def interrupt(self, name, args=dict()):
        interrupter = global_chom_chat.chat_state_defs[name](self)
        old = self.chat_state
        old.before_interrupt(interrupter, args)
        self.chat_states.append(interrupter)
        self.chat_state.on_enter(old, args, True)
        old.after_interrupt(interrupter, args)

    def next(self, name, args=dict()):
        if len(self.chat_states) == 0: return self.interrupt(name, args)
        to = global_chom_chat.chat_state_defs[name](self)
        old = self.chat_state
        old.on_next(to, args)
        self.chat_states[-1] = to
        self.chat_state.on_enter(old, args, False)

    def finish(self, args=dict()):
        from_ = self.chat_state
        from_.on_finish(args)
        self.chat_states.pop()
        self.chat_state.on_return(self, args)

    @property
    def chat_state(self):
        if len(self.chat_states) == 0: self.chat_states.append(global_chom_chat.chat_state_defs['_null'](self))
        return self.chat_states[-1]

    @chat_state.setter
    def chat_state(self, new_state):
        self.next(new_state)

    def perform_on_message(self, message: str):
        self.chat_state.on_message(message)