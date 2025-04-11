from sqlmodel import Field, SQLModel
from typing import Optional


class Providers(SQLModel, table=True):
    provider_id: Optional[int] = Field(
        default=None, primary_key=True)
    name: str
    lastname: str
    phone: str
