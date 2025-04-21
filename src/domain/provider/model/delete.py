from sqlmodel import select
from .schema import Provider
from common.utils.db_error_handler import DBErrorHandler


async def model_delete_provider(provider_id: int):
    async with DBErrorHandler() as _, _ as session:
        query = select(Provider).where(Provider.provider_id == provider_id)
        provider = (await session.exec(query)).one()
        await session.delete(provider)
        await session.commit()
