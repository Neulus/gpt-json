

from pydantic import BaseModel


class ChatCompletionDelta(BaseModel):
    content: str
    role: str 


class ChatCompletionChunkChoice(BaseModel):
    delta: ChatCompletionDelta
    finish_reason: str
    index: int


class ChatCompletionChunk(BaseModel):
    choices: list
    created: int
    id: str
    model: str
    object: str
