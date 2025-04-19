from config.database import db_session
from models.provider.schema import ProviderInsert, Provider


async def insert_provider(provider: ProviderInsert):
    async with db_session() as session:
        provider_schema = Provider(**provider.model_dump())
        session.add(provider_schema)
        await session.commit()
        await session.refresh(provider_schema)
        return {"created_id":  provider_schema.provider_id}
