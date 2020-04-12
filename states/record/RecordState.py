from __future__ import annotations
from typing import TYPE_CHECKING
from ChomChat.State.GroupState import GroupState
from states.record.RecordNameState import RecordNameState
from states.record.RecordTypeState import RecordTypeState
from states.record.RecordValueState import RecordValueState

if TYPE_CHECKING:
    from ChomChat import Context

class RecordState(GroupState):
    def __init__(self, parent, name, default=None):
        super().__init__(parent, name, default)

        # Register child state here
        self.type = RecordTypeState(self, 'type')
        self.name = RecordNameState(self, 'name')
        self.value = RecordValueState(self, 'value')

    # For Pycharm code hint
    def __get__(self, instance, owner):
        super().__get__(instance, owner)
        return self