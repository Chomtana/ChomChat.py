from __future__ import annotations

from typing import Dict, List, Callable, TYPE_CHECKING
from config import *


if TYPE_CHECKING:
    from ChomChat import Context

class Middleware:
    def on_message(self, context: Context, message: str):
        pass

    def on_message_return(self, context: Context, message: str):
        pass
