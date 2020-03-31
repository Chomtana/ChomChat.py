from sqlalchemy import create_engine

class ChomChatGlobalConfigBase:
  db: object = create_engine('sqlite://')