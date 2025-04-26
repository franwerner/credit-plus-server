from .schema import Client
from config.database import get_db_session


async def model_create_client(data: Client):
    async with get_db_session() as _, _ as session:
        client = Client(**data.model_dump())
        session.add(client)
        await session.commit()
        await session.refresh(client)
        return client
