from .schema import ProviderInsert, Provider
from common.utils.db_error_handler import DBErrorHandler
from sqlalchemy.exc import IntegrityError
from typing import Dict

error_messages = {
    IntegrityError: "Ese proveedor ya se encuentra existente."
}


async def model_create_provider(provider: ProviderInsert):
    async with DBErrorHandler(error_messages) as _, _ as session:
        provider_schema = Provider(**provider.model_dump())
        session.add(provider_schema)
        await session.commit()
        await session.refresh(provider_schema)
        return {"created_id":  provider_schema.provider_id}
