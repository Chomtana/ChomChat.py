from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Callable, List, Any

if TYPE_CHECKING:
    from ChomChat import Context

from ChomChat.Outputer.OutputerQueue import OutputerQueue
from ChomChat.Outputer.Component import Component
from ChomChat.Outputer.GlobalRegister import outputer_without_queue


class Outputer:
    context: Context

    queues: Dict[str, OutputerQueue]

    session_count: int = 0

    def __init__(self, context: Context):
        self.queues = {}

        self.context = context

    def send(self, message: Component):
        if self.session_count > 0:
            self.send_to_queue('_session', message)
        else:
            self.send_instant(message)

    def send_instant(self, message: Component):
        outputer_without_queue[self.context.user.provider_name](self, message)

    def send_to_queue(self, queue_name: str, message: Component):
        self.queues[queue_name].append(message)

    def create_queue(self, queue_name: str, metadata={}):
        return OutputerQueue(self, queue_name, metadata)

    def start_session(self, metadata={}):
        if self.session_count == 0 or '_session' not in self.queues:
            session = self.create_queue('_session', metadata)
        else:
            session = self.queues['_session']
        self.session_count += 1
        return session

    def end_session(self):
        if self.session_count < 1: return

        self.session_count -= 1
        if self.session_count == 0:
            self.queues['_session'].commit()

    def commit(self, queue_name='_session'):
        if queue_name == '_session' and self.session_count > 0:
            self.end_session()
        elif queue_name == '_session':
            raise Exception('Cannot commit output: Not in a session (maybe you forget queue_name)')
        else:
            self.queues[queue_name].commit()

    def clear(self, queue_name='_session'):
        self.queues[queue_name].clear()
