from sqlmodel import select
from config.database import get_db_session
from .schema import Client


async def model_delete_client(client_id: int):
    async with get_db_session() as _, _ as session:
        query = select(Client).where(Client.client_id == client_id)
        client = (await session.exec(query)).one()
        await session.delete(client)
        await session.commit()
