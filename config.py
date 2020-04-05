from sqlalchemy import create_engine

DEBUG_MODE = True
CHAT_STATE_DEBUG_MODE = True

DB: object = create_engine('sqlite://')

BLANK_USER_PICTURE_URL = "https://upload.wikimedia.org/wikipedia/commons/3/34/PICA.jpg"

# more configs in providers/.../config.py
