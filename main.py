import uvicorn
from fastapi import FastAPI, Request, Body
from ChomChat.ChomChat import ChatState, global_chom_chat
from ChomChat.Decorator import RegisterChatState
from config import ChomChatGlobalConfig

global_chom_chat.load_global_config(ChomChatGlobalConfig())

from app import app

from providers.line.api import *

@app.get("/")
def read_root():
  test = ChatState()
  test.name = "dsadas"
  return test


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
  return {"item_id": item_id, "q": q}

@RegisterChatState('test')
class Test(ChatState):
    pass

print(global_chom_chat.chat_state_defs)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)