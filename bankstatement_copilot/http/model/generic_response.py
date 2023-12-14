from pydantic import BaseModel
from typing import Generic, TypeVar
""" This file is automatically generated, please do not modify """

T1 = TypeVar("T1")
""" 请求结果 """
class GenericResponse(Generic[T1], BaseModel):
		# 可读结果码
		code: str = None
		data: T1 = None
		message: str = None