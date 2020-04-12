from __future__ import annotations
from typing import TYPE_CHECKING
from ChomChat.State.GroupState import GroupState
from ChomChat.State.State import State

if TYPE_CHECKING:
    from ChomChat import Context

class StateName(GroupState):
    def __init__(self, parent, name, default=None):
        super().__init__(parent, name, default)

        # Register child state here
        # self.record = RecordState(self, 'record')

    # For Pycharm code hint
    def __get__(self, instance, owner):
        super().__get__(instance, owner)
        return self
