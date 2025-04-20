from sqlmodel import delete
from sqlalchemy import CursorResult
from .schema import Provider
from common.utils.db_error_handler import DBErrorHandler


async def model_delete_provider(provider_id: int):
    async with DBErrorHandler() as _, _ as session:
        query = delete(Provider).where(Provider.provider_id == provider_id)
        affects: CursorResult = await session.exec(query)
        await session.commit()
        return affects.rowcount
