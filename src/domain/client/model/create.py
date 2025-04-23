from .schema import ClientInsert, Client
from common.utils.db_error_handler import DBErrorHandler


async def model_create_client(data: ClientInsert):
    async with DBErrorHandler() as _, _ as session:
        client = Client(**data.model_dump())
        session.add(client)
        await session.commit()
        await session.refresh(client)
        return client
