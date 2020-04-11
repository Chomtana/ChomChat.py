from sqlalchemy import Column, Integer, String, JSON, Text, UniqueConstraint, Index, DateTime
from sqlalchemy.orm import relationship
from config import DB_SQL_BASE
from datetime import datetime


class UserCenter(DB_SQL_BASE):
    __tablename__ = 'chomchat_users_center'

    id = Column(Integer, primary_key=True)

    users_raw = relationship("UserRaw", back_populates="user_center")

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return "<UserCenter(id=%d)>" % (
            self.id if self.id is not None else -1
        )
