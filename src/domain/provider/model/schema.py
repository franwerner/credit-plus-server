from sqlmodel import Field, SQLModel, UniqueConstraint
from typing import Optional


class Provider(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint(
            "name", "lastname",
            name="provider_name_lastname_unique"
        ),
    )
    provider_id: Optional[int] = Field(primary_key=True)
    name: str
    lastname: str
    phone: Optional[str] = None


class ProviderInsert(SQLModel):
    name: str
    lastname: str
    phone: Optional[str] = None


class ProviderUpdate(SQLModel):
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone: Optional[str] = None
