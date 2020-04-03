from __future__ import annotations

from typing import Dict, List, Callable, TYPE_CHECKING
from config import *

if TYPE_CHECKING:
    from ChomChat import Context


class ChatState:
    context: Context
    name: str

    def __init__(self, context: Context):
        self.context = context

    def on_enter(self, from_: ChatState, args, is_interrupt: bool):
        if DEBUG_MODE and CHAT_STATE_DEBUG_MODE:
            print(f'[CSDBG] User "{self.context.user.display_name}" ENTER {self.name} with args {str(args)} {"INTERRUPT" if is_interrupt else ""}')

    def on_message(self, message: str):
        if DEBUG_MODE and CHAT_STATE_DEBUG_MODE:
            print(f'[CSDBG] User "{self.context.user.display_name}" MESSAGE {self.name} with message "{message}"')

    def on_finish(self, args):
        if DEBUG_MODE and CHAT_STATE_DEBUG_MODE:
            return_to = self.context.chat_states[-2].name if len(self.context.chat_states) > 1 else "_null"
            print(f'[CSDBG] User "{self.context.user.display_name}" FINISH {self.name} with args {str(args)} and will return to {return_to}')

    def on_next(self, to: ChatState, args):
        if DEBUG_MODE and CHAT_STATE_DEBUG_MODE:
            print(f'[CSDBG] User "{self.context.user.display_name}" NEXT FROM {self.name} TO {to.name} with args {str(args)}')

    def on_return(self, from_: ChatState, args):
        if DEBUG_MODE and CHAT_STATE_DEBUG_MODE:
            print(f'[CSDBG] User "{self.context.user.display_name}" RETURN TO {self.name} FROM {from_.name} with args {str(args)}')

    def before_interrupt(self, by: ChatState, args):
        if DEBUG_MODE and CHAT_STATE_DEBUG_MODE:
            print(f'[CSDBG] User "{self.context.user.display_name}" BEFORE INTERRUPT {self.name} with args {str(args)}')

    def after_interrupt(self, by: ChatState, args):
        if DEBUG_MODE and CHAT_STATE_DEBUG_MODE:
            print(f'[CSDBG] User "{self.context.user.display_name}" AFTER INTERRUPT{self.name} with args {str(args)}')