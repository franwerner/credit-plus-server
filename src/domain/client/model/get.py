from sqlmodel import select, or_
from common.utils.db_error_handler import DBErrorHandler
from .schema import Client


async def model_get_client(client_id: int):
    async with DBErrorHandler() as session:
        query = select(Client).where(Client.client_id == client_id)
        res = (await session.exec(query)).first()
        return res


async def model_get_clients(page: int, name_lastname: str):
    page_limit = 15
    query = select(Client).limit(page_limit)

    if page is not None:
        query = query.offset(page * page_limit)

    if name_lastname is not None:
        query = query.where(
            or_(
                Client.name == name_lastname,
                Client.lastname.like(name_lastname + '%')
            )
        )
    async with DBErrorHandler() as session:
        return (await session.exec(query)).all()
