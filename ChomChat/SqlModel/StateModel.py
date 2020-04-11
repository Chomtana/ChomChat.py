from sqlalchemy import Column, Integer, String, JSON, Text, UniqueConstraint, Index, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from config import DB_SQL_BASE, DB
from datetime import datetime


class StateModel(DB_SQL_BASE):
    __tablename__ = 'chomchat_states'

    id = Column(Integer, primary_key=True)
    user_center_id = Column(Integer, ForeignKey('chomchat_users_center.id'), nullable=False)
    user_center = relationship("UserCenter", back_populates="states")
    key = Column(String(1023), index=True, nullable=False)
    value = Column(JSON)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_at = Column(DateTime)

    __table_args__ = (
        Index('user_center_id_key_index', 'user_center_id', 'key')
    )

    def __repr__(self):
        return "<State(user_center_id='%d', key='%s')>" % (
            self.user_center_id, self.key)

    def delete(self):
        self.deleted_at = datetime.now()
