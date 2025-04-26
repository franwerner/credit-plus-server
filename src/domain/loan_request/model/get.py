from sqlmodel import select
from config.database import get_db_session
from .schema import LoanRequest


async def get_loan_request(loan_request_id: int):
    query = select(LoanRequest).where(
        LoanRequest.loan_request_id == loan_request_id)
    async with get_db_session() as session:
        res = (await session.exec(query)).first()
        return res


async def get_loan_requests(page: int = 0, client_id: int = None):
    page_limit = 15
    query = select(LoanRequest).limit(page_limit).offset(page * page_limit)
    if client_id:
        query.where(LoanRequest.client_fk == client_id)

    async with get_db_session() as session:
        res = (await session.exec(query)).all()
        return res
