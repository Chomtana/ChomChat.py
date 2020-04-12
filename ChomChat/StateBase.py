from __future__ import annotations

from typing import Dict, List, Callable, TYPE_CHECKING

from ChomChat.SqlModel.StateModel import StateModel
from config import *

if TYPE_CHECKING:
    from ChomChat import Context


class StateBase:
    _parent: StateBase
    _context: Context
    _name: str
    _backprop: bool
    _is_state: bool = False
    _self_mode: bool = False

    _model_added: bool = False

    #_children: List[StateBase]

    def __init__(self, parent, name, default=None):
        self._children = []
        self._backprop = False
        self._default = default

        self._parent = parent
        if parent is not None:
            self._context = parent._context

        self._name = name

        print(self.path())

        '''
        for (key, value) in self.__class__.__dict__.items():
            if not key[0] == '_' and isinstance(value, StateBase) and value._is_state:
                self._children.append(value)
        '''


        self._model = DB.query(StateModel).filter(
            StateModel.user_center_id == self._context.user.center.id,
            StateModel.key == self.path(),
            StateModel.deleted_at == None,
        ).one_or_none()

        self._model_added = True

        if self._model is None:
            self._model_added = False
            self._model = StateModel(user_center_id=self._context.user.center.id, key=self.path(), value=default)
            #DB.add(self._model)

        self._self_mode = False

        self._is_state = True

    def path(self):
        if self._parent is None:
            return self._name
        return self._parent.path() + '.' + self._name

    def __get__(self, instance, owner):
        if not self._is_state: raise Exception('You forget to call super().__init__(parent, name) in some state')

        self._before_get('')
        self.before_get('')

        if self._self_mode:
            return self

        if self._model.deleted_at is None:
            return self._model.value
        else:
            return None

    def __set__(self, instance, value):
        if not self._is_state: raise Exception('You forget to call super().__init__(parent, name) in some state')

        old = self._model.value
        self._before_set(value, old, '')
        self.before_set(value, old, '')
        self._model.value = value
        self._after_set(value, old, '')
        self.after_set(value, old, '')

        if not self._model_added:
            DB.add(self._model)

    def __delete__(self, instance):
        if not self._is_state: raise Exception('You forget to call super().__init__(parent, name) in some state')

        old = self._model.value
        self._before_delete(old, '')
        self.before_delete(old, '')
        #del self._value
        #self._value = None
        if self._model_added:
            DB.delete(self._model)
        self._after_delete(old, '')
        self.after_delete(old, '')

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