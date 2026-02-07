from typing import List
from pydantic import BaseModel

class PayloadCreate(BaseModel):
    list_1: List[str]
    list_2: List[str]

class PayloadResponse(BaseModel):
    id: int

class PayloadOutput(BaseModel):
    output: str
