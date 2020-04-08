from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import timedelta

DEBUG_MODE = True
CHAT_STATE_DEBUG_MODE = True

DB_SQL_ENGINE = create_engine('sqlite:///:memory:', echo=True)
DB_SQL_BASE = declarative_base()
DB = sessionmaker(bind=DB_SQL_ENGINE)()

BLANK_USER_PICTURE_URL = "https://upload.wikimedia.org/wikipedia/commons/3/34/PICA.jpg"
USER_DATA_EXPIRE_IN = timedelta(days=1)

# more configs in providers/.../config.py

