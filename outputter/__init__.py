from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Callable

if TYPE_CHECKING:
    from ChomChat import Context


class Outputer:
    context: Context

    with_queue: Dict[str, Callable] = {}
    without_queue: Dict[str, Callable] = {}

    in_session: bool = False

    def __init__(self, context: Context):
        self.context = context

    def send(self, message):
        if self.in_session:
            self.send_queue('_session', message)
        else:
            self.send_instant(message)

    def send_instant(self, message):
        pass

    def send_queue(self, queue_name: str, message):
        pass
