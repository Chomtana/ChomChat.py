from __future__ import annotations

from typing import Dict, List, Callable, TYPE_CHECKING

from ChomChat.SqlModel.UserRaw import UserRaw
from config import *
from ChomChat import Context
from sql_models.UserCenter import UserCenter
from datetime import datetime


class User:
    provider_name: str
    id: str

    display_name: str
    picture_url: str
    raw: object

    context: Context

    raw_model: UserRaw
    center: UserCenter

    created_at: datetime
    updated_at: datetime

    def __init__(
        self, provider_name, id_, display_name, raw,
        picture_url = BLANK_USER_PICTURE_URL
    ):
        self.update(provider_name, id_, display_name, raw, picture_url)

    def update(
        self, provider_name, id_, display_name, raw,
        picture_url=BLANK_USER_PICTURE_URL
    ):
        self.provider_name = provider_name
        self.id = id_
        self.display_name = display_name
        self.picture_url = picture_url
        self.raw = raw

        self.raw_model = DB.query(UserRaw).filter(UserRaw.provider_name == provider_name, UserRaw.provider_id == id_).one_or_none()

        if self.raw_model is None:
            with DB.begin(subtransactions=True):
                self.center = UserCenter()
                DB.add(self.center)
                DB.flush()

                self.raw_model = UserRaw(provider_name=provider_name, provider_id=id_, display_name=display_name, picture_url=picture_url, raw=raw.json(), user_center_id=self.center.id)
                DB.add(self.raw_model)
        else:
            self.raw_model.display_name = display_name
            self.raw_model.picture_url = picture_url
            self.raw_model.raw = raw.json()
            DB.commit()

        self.center = self.raw_model.user_center

        self.created_at = self.raw_model.created_at
        self.updated_at = self.raw_model.updated_at

        self.context = Context(self)

    def expired(self):
        return datetime.now() > self.updated_at + USER_DATA_EXPIRE_IN
