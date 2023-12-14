from pydantic import BaseModel
from typing import Generic, TypeVar


class OcrRequest(BaseModel):
    input: str = None
    secret_key: str = None
    file_path: str = None
