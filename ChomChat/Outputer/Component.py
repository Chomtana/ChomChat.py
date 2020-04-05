from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Callable, List, Any

if TYPE_CHECKING:
    from ChomChat import Context

from ChomChat.Outputer.ComponentCannotFormatException import ComponentCannotFormatException


class Component:
    name: str

    def format_line(self):
        raise ComponentCannotFormatException(self, 'line')

    def format(self, provider_name: str):
        key = 'format_'+provider_name

        if key in self.__class__.__dict__:
            return self.__class__.__dict__[key](self)

        raise ComponentCannotFormatException(self, provider_name)
