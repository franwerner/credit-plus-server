from config.database import db_session
from models.provider import ProviderInsert, Provider


async def insert_provider(provider: ProviderInsert):
    async with db_session() as session:
        session.add(Provider(**provider.model_dump()))
        await session.commit()
