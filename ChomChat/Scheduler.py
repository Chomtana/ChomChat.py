from __future__ import annotations

from datetime import timedelta, datetime
from typing import Dict, List, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ChomChat import Context

from threading import Timer as TimerBase


class Timer:
    timer: TimerBase
    scheduler: Scheduler
    context: Context
    __due: datetime
    name: str
    is_pausing: bool

    def __init__(self, interval: float, function, args=None, kwargs=None, context=None, scheduler=None):
        self.context = context
        self.scheduler = scheduler

        self.timer = TimerBase(interval, function, (self, *args), kwargs)

        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs

        self.__due = datetime.now() + timedelta(seconds=self.interval)
        self.name = None
        self.is_pausing = False

    def get_due(self):
        return self.__due

    def set_due(self, due: datetime, one_time = True):
        if one_time:
            self.timer.restart(due)
            self.__due = due    # To make value perfectly accurate
        else:
            self.set_interval(due)
        return self

    def set_interval(self, interval):
        self.restart(interval, True)
        return self

    def get_remaining_time(self):
        return self.__due - datetime.now()

    def start(self, overtime = True):
        if not self.is_pausing:
            self.timer.start()
        else:
            if overtime or datetime.now() <= self.__due:
                self.restart(max(self.get_remaining_time().total_seconds(), 0))
            self.is_pausing = False

    def cancel(self):
        self.timer.cancel()
        self.is_pausing = False
        if self.name is not None:
            del self.scheduler.store[self.name]

    def pause(self):
        self.timer.cancel()
        self.is_pausing = True

    def restart(self, interval=None, change_interval=False):
        if interval is None:
            interval = self.interval
        elif isinstance(interval, datetime):
            interval = (interval - datetime.now()).total_seconds()
        elif isinstance(interval, timedelta):
            interval = interval.total_seconds()

        self.timer.cancel()
        self.timer = TimerBase(interval, self.function, (self, *self.args), self.kwargs)
        self.timer.start()
        self.__due = datetime.now() + timedelta(seconds=interval)

        if change_interval:
            self.interval = interval

    def register_to_store(self, name: str):
        self.scheduler.store[name] = self


def set_interval_inner(timer: Timer, f, *args, **kwargs):
    timer.restart()
    f(timer, *args, **kwargs)


def schedule_interval_inner(timer: Timer, f, interval, *args, **kwargs):
    timer.function = set_interval_inner
    timer.args = (f, *args)
    timer.restart(interval, True)
    f(timer, *args, **kwargs)


class Scheduler:
    context: Context
    store: Dict[str, Timer]

    def __init__(self, context: Context):
        self.context = context

    def set_timeout(self, f, timeout, *args, **kwargs):
        if isinstance(timeout, datetime):
            timeout = max( (timeout - datetime.now()).total_seconds(), 0 )
        elif isinstance(timeout, timedelta):
            timeout = timeout.total_seconds()

        timer = Timer(timeout, f, args, kwargs, context=self.context, scheduler=self)
        timer.start()
        return timer

    def set_interval(self, f, interval, *args, **kwargs):
        if isinstance(interval, timedelta):
            interval = interval.total_seconds()

        timer = Timer(interval, set_interval_inner, (f, *args), kwargs, context=self.context, scheduler=self)
        timer.start()
        return timer

    def schedule_interval(self, f, start, interval, *args, **kwargs):
        return self.set_timeout(schedule_interval_inner, start, f, interval, *args, **kwargs)
