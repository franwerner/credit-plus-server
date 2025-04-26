from sqlmodel import Field, SQLModel, UniqueConstraint, Column, String
from typing import Optional
from sqlalchemy.schema import CreateTable

from config.database import engine


class Client(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint(
            "name", "lastname", "provider_fk",
            name="unique_client_provider"
        ),
    )

    client_id: Optional[int] = Field(primary_key=True)
    name: str = Field(max_length=45)
    lastname: str = Field(max_length=45)
    phone: Optional[int]
    provider_fk: int = Field(foreign_key="provider.provider_id")


print(str(CreateTable(Client.__table__).compile(dialect=engine.dialect)))


class ClientUpdate(SQLModel):
    name: Optional[str]
    lastname: Optional[str]
    phone: Optional[str]
