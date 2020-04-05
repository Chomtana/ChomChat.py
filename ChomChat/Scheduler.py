from __future__ import annotations

from datetime import timedelta, datetime
from typing import Dict, List, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ChomChat import Context

from threading import Timer


class Scheduler:
    context: Context

    def __init__(self, context: Context):
        self.context = context

    def set_timeout(self, f, timeout, *args):
        if isinstance(timeout, datetime):
            timeout = max( (timeout - datetime.now()).total_seconds(), 0 )
        elif isinstance(timeout, timedelta):
            timeout = timeout.total_seconds()
        timer = Timer(timeout, f, (self.context, *args))
        timer.start()
