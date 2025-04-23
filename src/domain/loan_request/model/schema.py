from datetime import timezone
from sqlmodel import SQLModel, Field, Enum, Column, String, Float, TIMESTAMP
from typing import Optional
import datetime

client_fk = Field(foreign_key="Client.client_id")
refinancing_fk = Field(foreign_key="Loan_request.loan_request_id", nullable=True)


class Status(str, Enum):
    completed = "completed"
    refinanced = "refinanced"
    canceled = "canceled"
    defaulted = "defaulted"
    pending = "pending"


class LoanRequest(SQLModel, table=True):
    loan_request_id: Optional[int] = Field(primary_key=True)
    total: int = Field(nullable=False)
    expired_at: datetime = Field(nullable=False, sa_column=Column(TIMESTAMP(timezone=True)))
    create_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.datetime.now(timezone.utc),
        nullable=False,
        sa_column=Column(TIMESTAMP(timezone=True)))
    status: str = Field(sa_column=Column(Status), default=Status.pending)
    description: str = Field(sa_column=Column(String(255)))
    percentage: float = Field(sa_column=Column(Float(2, 2)), nullable=False)
    refinancing_fk: Optional[int] = refinancing_fk
    client_fk: Optional[int] = client_fk
