from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Callable, List, Any

if TYPE_CHECKING:
    from ChomChat.Outputer import Outputer, Component, DoNotDestroyQueue

from ChomChat.Outputer.GlobalRegister import outputer_with_queue
from ChomChat.Outputer.DoNotDestroyQueue import DoNotDestroyQueue


class OutputerQueue:
    outputer: Outputer
    name: str
    metadata: Any
    data: List[Component] = []

    def __init__(self, outputer: Outputer, name: str, metadata):
        self.outputer = outputer
        self.name = name
        self.metadata = metadata

        outputer.queues[name] = self

    def append(self, item: Component):
        self.data.append(item)

    def commit(self):
        if len(self.data) > 0:
            try:
                outputer_with_queue[self.outputer.context.user.provider_name](self)
            except DoNotDestroyQueue:
                return
            except Exception as err:
                del self.outputer.queues[self.name]
                raise err
        del self.outputer.queues[self.name]

    def format(self, provider_name: str):
        res = []
        for d in self.data:
            res.append(d.format(provider_name))
        return res