from __future__ import annotations
from typing import TYPE_CHECKING
from ChomChat.State.GroupState import GroupState
from states.record.RecordState import RecordState

if TYPE_CHECKING:
    from ChomChat import Context


class RootState(GroupState):
    _context: Context

    def __init__(self, context: Context):
        self._context = context

        super().__init__(None, 'root')

        # Register child state here
        self.record = RecordState(self, 'record')

    # For Pycharm code hint
    def __get__(self, instance, owner):
        super().__get__(instance, owner)
        return self
