from __future__ import annotations

from typing import Dict, List, Callable, TYPE_CHECKING
from config import *


if TYPE_CHECKING:
    from ChomChat import Context


class ChomChat:
    chat_state_defs: Dict[str, type] = {}
    contexts: Dict[str, Context] = {}
    context_builders: Dict[str, Callable] = {}
    context_getters: Dict[str, Callable] = {}

    def register_chat_state(self, name: str, chat_state_class: type):
        self.chat_state_defs[name] = chat_state_class;

    def register_context_builder(self, provider_name: str, f: Callable):
        self.context_builders[provider_name] = f

    def register_context_getter(self, provider_name: str, f: Callable):
        self.context_getters[provider_name] = f

    def build_context(self, provider_name: str, raw_data):
        return self.context_builders[provider_name](raw_data)

    def get_context(self, provider_name: str, id_: str, raw_data=None):
        key = provider_name + ' ' + id_
        if raw_data is None: return self.contexts[key]
        if key in self.contexts: return self.contexts[key]
        self.contexts[key] = self.build_context(provider_name, raw_data)
        return self.contexts[key]

    def get_context_by_raw(self, provider_name: str, raw_data):
        return self.context_getters[provider_name](raw_data)


global_chom_chat = ChomChat()
