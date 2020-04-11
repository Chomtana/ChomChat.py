from sqlalchemy import Column, Integer, String, JSON, Text, UniqueConstraint, Index, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from config import DB_SQL_BASE
from datetime import datetime


class UserRaw(DB_SQL_BASE):
    __tablename__ = 'chomchat_users_raw'

    id = Column(Integer, primary_key=True)
    provider_name = Column(String, nullable=False, index=True)
    provider_id = Column(String(255), nullable=False, index=True)

    display_name = Column(Text, nullable=False)
    picture_url = Column(Text, nullable=False)
    raw = Column(JSON)

    user_center_id = Column(Integer, ForeignKey('chomchat_users_center.id'), nullable=False)
    user_center = relationship("UserCenter", back_populates="users_raw")

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    __table_args__ = (
        UniqueConstraint('provider_name', 'provider_id'),
        Index('provider_name_provider_id_index', 'provider_name', 'provider_id')
    )

    def __repr__(self):
        return "<UserRaw(provider_name='%s', provider_id='%s', display_name='%s', picture_url='%s', user_center_id='%d')>" % (
            self.provider_name, self.provider_id, self.display_name, self.picture_url, self.user_center_id)
