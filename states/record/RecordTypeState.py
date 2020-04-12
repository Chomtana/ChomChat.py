from __future__ import annotations
from typing import TYPE_CHECKING
from ChomChat.State.GroupState import GroupState
from ChomChat.State.StrState import StrState

if TYPE_CHECKING:
    from ChomChat import Context

class RecordTypeState(StrState):
    TYPE_FOOD_BEVERAGE = "food_beverage"

    def __init__(self, parent, name, default=None):
        super().__init__(parent, name, default)
