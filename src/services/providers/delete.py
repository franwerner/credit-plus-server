from sqlmodel import delete
from config.database import db_session
from models.provider import Provider


async def delete_provider(provider_id: int):
    async with db_session() as session:
        query = delete(Provider).where(Provider.provider_id == provider_id)
        await session.exec(query)
        await session.commit()
