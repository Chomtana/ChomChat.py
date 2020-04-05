from __future__ import annotations
from typing import TYPE_CHECKING
from ChomChat import StateBase

if TYPE_CHECKING:
    from ChomChat import Context


class RootState(StateBase):
    context: Context

    def __init__(self, context: Context):
        self.context = context
        self.value = None
        super().__init__(None, '_root')
