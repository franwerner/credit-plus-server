from .schema import ClientUpdate, Client
from common.utils.db_error_handler import DBErrorHandler
from sqlmodel import select


async def model_update_client(client_id: int, client_data: ClientUpdate):
    async with DBErrorHandler() as _, _ as session:
        query = select(Client).where(Client.client_id == client_id)
        update_data = client_data.model_dump(exclude_unset=True)
        client = (await session.exec(query)).one()
        for key, value in update_data.items():
            setattr(client, key, value)
        await session.commit()
        await session.refresh(client)
        return client
