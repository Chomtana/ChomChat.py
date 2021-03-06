import uvicorn
from fastapi import FastAPI, Request, Body
from ChomChat import ChatState
from ChomChat.ChomChat import global_chom_chat
from ChomChat.Decorator import RegisterChatState

from config import *
from app import app

# Init providers
from providers.line.api import *

# Init chat states
import chat_states
import sql_models

DB_SQL_BASE.metadata.create_all(DB_SQL_ENGINE)


@app.get("/")
def read_root():
  test = ChatState()
  test.name = "dsadas"
  return test


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
  return {"item_id": item_id, "q": q}

print(global_chom_chat.chat_state_defs)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)