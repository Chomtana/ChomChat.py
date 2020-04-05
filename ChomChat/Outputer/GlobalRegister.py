from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Callable, List, Any

outputer_with_queue: Dict[str, Callable] = {}
outputer_without_queue: Dict[str, Callable] = {}


def register_with_queue(provider_name: str, f: Callable):
    outputer_with_queue[provider_name] = f


def register_without_queue(provider_name: str, f: Callable):
    outputer_without_queue[provider_name] = f