from typing import Optional
from sqlmodel import SQLModel, Field

class TransformedString(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    original: str = Field(index=True)
    transformed: str

class Payload(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    cache_key: str = Field(index=True, unique=True)
    output: str
