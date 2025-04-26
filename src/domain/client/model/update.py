from sqlmodel import select
from config.database import get_db_session
from .schema import ClientUpdate, Client


async def model_update_client(client_id: int, client_data: ClientUpdate):
    async with get_db_session() as _, _ as session:
        query = select(Client).where(Client.client_id == client_id)
        update_data = client_data.model_dump(exclude_unset=True)
        client = (await session.exec(query)).one()
        for key, value in update_data.items():
            setattr(client, key, value)
        await session.commit()
        await session.refresh(client)
        return client
