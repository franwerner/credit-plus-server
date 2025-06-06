from sqlmodel import select, or_
from config.database import get_db_session

from .schema import Client


async def model_get_client(client_id: int):
    async with get_db_session() as session:
        query = select(Client).where(Client.client_id == client_id)
        return (await session.exec(query)).first()


async def model_get_clients(page: int = 0, name_lastname: str = None, provider_id: int = None):
    page_limit = 15
    query = (select(Client)
             .where(Client.provider_fk == provider_id)
             .limit(page_limit)
             .offset(page * page_limit)
             )

    if name_lastname is not None:
        query = query.where(
            or_(
                Client.name == name_lastname,
                Client.lastname.like(name_lastname + '%')
            )
        )
    async with get_db_session() as session:
        return (await session.exec(query)).all()
