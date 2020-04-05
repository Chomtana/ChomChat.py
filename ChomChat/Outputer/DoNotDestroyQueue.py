from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Callable, List, Any

if TYPE_CHECKING:
    from ChomChat.Outputer import OutputerQueue


class DoNotDestroyQueue(Exception):
    def __init__(self, queue: OutputerQueue):
        super().__init__(f'Request queue not to destroy "{queue.name}" of user "{queue.outputer.context.user.display_name}" FAILED!')