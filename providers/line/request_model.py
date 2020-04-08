from typing import List, Dict, Optional
from pydantic import BaseModel
from pydantic_config import PydanticConfig


class LineUser(BaseModel):
    displayName: str
    userId: str
    pictureUrl: str
    statusMessage: str

    Config = PydanticConfig


class LineRequestSource(BaseModel):
    userId: str
    type: str

    Config = PydanticConfig


class LineRequestEvent(BaseModel):
    type: str
    replyToken: str
    source: LineRequestSource
    timestamp: int
    message: Dict[str, str]

    mode: Optional[str]
    user: Optional[LineUser]
    destination: Optional[str]

    Config = PydanticConfig


class LineRequest(BaseModel):
    events: List[LineRequestEvent]
    destination: Optional[str]

    Config = PydanticConfig
