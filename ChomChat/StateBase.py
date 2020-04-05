from __future__ import annotations

from typing import Dict, List, Callable, TYPE_CHECKING
from config import *

if TYPE_CHECKING:
    from ChomChat import Context

class StateBase:
    _parent: StateBase
    _context: Context
    _name: str
    _backprop: bool = False
    _is_state: bool = False

    _children: List[StateBase]

    def __init__(self, parent, name, default=None):
        self._children = []

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