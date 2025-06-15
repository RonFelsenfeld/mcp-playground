from pydantic import BaseModel
from enum import Enum


class ResponseStatus(Enum):
    SUCCESS = "success"
    ERROR = "error"


class BasicResponse(BaseModel):
    message: str
    status: ResponseStatus
