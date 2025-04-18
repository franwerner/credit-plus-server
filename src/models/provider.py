from sqlmodel import Field, SQLModel
from typing import Optional


class Provider(SQLModel, table=True):
    provider_id: Optional[int] = Field(
        default=None, primary_key=True)
    name: str
    lastname: str
    phone: str


class ProviderInsert(SQLModel):
    name: str
    lastname: str
    phone: str
