from typing import List, Dict, Optional
from pydantic import BaseModel


class LineUser(BaseModel):
    displayName: str
    userId: str
    pictureUrl: str
    statusMessage: str


class LineRequestSource(BaseModel):
    userId: str
    type: str


class LineRequestEvent(BaseModel):
    type: str
    replyToken: str
    source: LineRequestSource
    timestamp: int
    mode: Optional[str]
    message: Dict[str, str]
    user: Optional[LineUser]
    destination: Optional[str]


class LineRequest(BaseModel):
    events: List[LineRequestEvent]
    destination: Optional[str]
