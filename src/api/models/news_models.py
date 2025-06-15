from pydantic import BaseModel
from enum import Enum


class Article(BaseModel):
    title: str | None = None
    description: str | None = None
    url: str | None = None


class ResponseStatus(Enum):
    SUCCESS = "success"
    ERROR = "error"


class NewsResponse(BaseModel):
    data: list[Article]
    status: ResponseStatus
