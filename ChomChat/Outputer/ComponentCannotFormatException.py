from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Callable, List, Any

if TYPE_CHECKING:
    from ChomChat.Outputer import Component


class ComponentCannotFormatException(Exception):
    def __init__(self, component: Component, provider_name: str):
        super().__init__(f'Cannot format component "{component.name}" into "{provider_name}" format')