from sqlalchemy import create_engine

class ChomChatGlobalConfigBase:
  db: object = create_engine('sqlite://')

  BLANK_USER_PICTURE_URL = "https://upload.wikimedia.org/wikipedia/commons/3/34/PICA.jpg"