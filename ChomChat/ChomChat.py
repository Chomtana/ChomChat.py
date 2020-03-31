from __future__ import annotations

from ChomChat.ChomChatGlobalConfigBase import ChomChatGlobalConfigBase
from typing import Dict, List, Callable


class ChomChat:
    global_config: ChomChatGlobalConfigBase
    chat_state_defs: Dict[str, type] = {}
    contexts: Dict[str, Context] = {}
    context_builders: Dict[str, Callable] = {}

    def load_global_config(self, global_config):
        self.global_config = global_config

    def register_chat_state(self, name: str, chat_state_class: type):
        self.chat_state_defs[name] = chat_state_class;

    def register_context_builder(self, provider_name: str, f: Callable):
        self.context_builders[provider_name] = f

    def build_context(self, provider_name: str, id_: str, raw_data):
        return self.context_builders[provider_name](id_, raw_data)

    def get_context(self, provider_name: str, id_: str, raw_data=None):
        key = provider_name + ' ' + id_
        if raw_data is None: return self.contexts[key]
        if key in self.contexts: return self.contexts[key]
        self.contexts[key] = self.build_context(provider_name, id_, raw_data)
        return self.contexts[key]

global_chom_chat = ChomChat()

class User:
    display_name: str
    id: str
    provider_name: str
    context: Context
    raw: object


class Context:
    chom_chat: ChomChat
    chat_states: List[ChatState] = []
    state: StateBase
    user: User

    def __init__(self, user: User, chom_chat: ChomChat = global_chom_chat):
        user.context = self
        chom_chat.contexts[user.id] = self

        self.user = user
        self.chom_chat = chom_chat

        self.interrupt('_start')

    def interrupt(self, name, args=dict()):
        interrupter = self.chom_chat.chat_state_defs[name](self)
        old = self.chat_state
        old.before_interrupt(interrupter, args)
        self.chat_states.append(interrupter)
        self.chat_state.on_enter(old, args, True)
        old.after_interrupt(interrupter, args)

    def next(self, name, args=dict()):
        if len(self.chat_states) == 0: return self.interrupt(name, args)
        to = self.chom_chat.chat_state_defs[name](self)
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
        if len(self.chat_states) == 0: self.chat_states.append(self.chom_chat.chat_state_defs['_null'](self))
        return self.chat_states[-1]

    @chat_state.setter
    def chat_state(self, new_state):
        self.next(new_state)

    def perform_on_message(self, message: str):
        self.chat_state.on_message(message)


class ChatState:
    context: Context

    def __init__(self, context: Context):
        self.context = context

    def on_enter(self, from_: ChatState, args, is_interrupt: bool):
        pass

    def on_return(self, from_: ChatState, args):
        pass

    def on_message(self, message: str):
        pass

    def on_finish(self, args):
        pass

    def on_next(self, to: ChatState, args):
        pass

    def before_interrupt(self, by: ChatState, args):
        pass

    def after_interrupt(self, by: ChatState, args):
        pass


class StateBase:
    _parent: StateBase
    _context: Context
    _name: str
    _backprop: bool = False
    _is_state: bool = False

    _children: List[StateBase] = []

    def __init__(self, parent, name, default=None):
        self._parent = parent
        self._context = parent.context
        self._name = name
        self._value = self.load_value() or default
        for (key, value) in self.__class__.__dict__.items():
            if not key[0] == '_' and isinstance(value, StateBase) and value._is_state:
                self._children.append(value)
        self._is_state = True

    def __get__(self, instance, owner):
        if not self._is_state: raise Exception('You forget to call super().__init__(parent, name) in some state')

        self._before_get('')
        self.before_get('')
        return self._value

    def __set__(self, instance, value):
        if not self._is_state: raise Exception('You forget to call super().__init__(parent, name) in some state')

        old = self._value
        self._before_set(value, old, '')
        self.before_set(value, old, '')
        self._value = value
        self._after_set(value, old, '')
        self.after_set(value, old, '')

    def __delete__(self, instance):
        if not self._is_state: raise Exception('You forget to call super().__init__(parent, name) in some state')

        old = self._value
        self._before_delete(old, '')
        self.before_delete(old, '')
        del self._value
        self._value = None
        self._after_delete(old, '')
        self.after_delete(old, '')

    def load_value(self):
        return None

    def _before_get(self, path):
        pass

    def before_get(self, path):
        pass

    def _before_set(self, value, old, path):
        pass

    def before_set(self, value, old, path):
        pass

    def _after_set(self, value, old, path):
        pass

    def after_set(self, value, old, path):
        pass

    def _before_delete(self, old, path):
        pass

    def before_delete(self, old, path):
        pass

    def _after_delete(self, old, path):
        pass

    def after_delete(self, old, path):
        pass
