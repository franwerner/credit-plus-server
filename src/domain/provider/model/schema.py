from typing import Optional
from sqlmodel import Field, SQLModel, UniqueConstraint, String, Column, Enum


class Role(str, Enum):
    admin = "admin"
    loan = "loan"
    investor = "investor"


class Provider(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint(
            "name", "lastname",
            name="provider_name_lastname_unique"
        ),
    )
    provider_id: Optional[int] = Field(primary_key=True)
    name: str = Field(max_length=45, sa_column=Column(String(45)))
    lastname: str = Field(max_length=45, sa_column=Column(String(45)))
    phone: Optional[str] = None
    role: Optional[str] = Field(sa_column=Column(Role), default=Role.loan)

    class Config:
        validate_assignment = True


class ProviderUpdate(SQLModel):
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone: Optional[str] = None
