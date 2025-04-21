
from sqlmodel import Field, SQLModel, UniqueConstraint
from typing import Optional

provider_fk = Field(foreign_key="provider.provider_id")


class Client(SQLModel, table=True):

    __table_args__ = (
        UniqueConstraint(
            "name", "lastname",
            name="client_name_lastname_unique"
        ),
    )

    client_id: Optional[int] = Field(primary_key=True)
    name: str
    lastname: str
    phone: str
    provider_fk: Optional[int] = provider_fk


class ClientInsert(SQLModel):
    name: str
    lastname: str
    phone: Optional[str]
    provider_fk: int = provider_fk


class ClientUpdate(SQLModel):
    name: Optional[str]
    lastname: Optional[str]
    phone: Optional[str]
