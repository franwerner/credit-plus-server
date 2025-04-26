from sqlmodel import select
from .schema import Provider
from config.database import get_db_session


async def model_delete_provider(provider_id: int):
    async with get_db_session() as _, _ as session:
        query = select(Provider).where(Provider.provider_id == provider_id)
        provider = (await session.exec(query)).one()
        await session.delete(provider)
        await session.commit()
