from __future__ import annotations

from typing import Dict, List, Callable, TYPE_CHECKING
from config import *

from ChomChat import Context


class User:
    provider_name: str
    id: str

    display_name: str
    picture_url: str
    raw: object

    context: Context

    def __init__(
        self, provider_name, id_, display_name, raw,
        picture_url = BLANK_USER_PICTURE_URL
    ):
        self.provider_name = provider_name
        self.id = id_
        self.display_name = display_name
        self.picture_url = picture_url
        self.raw = raw
        self.context = Context(self)
