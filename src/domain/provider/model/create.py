from config.database import get_db_session
from .schema import Provider


async def model_create_provider(provider: Provider):
    async with get_db_session() as _, _ as session:
        provider_schema = Provider(**provider.model_dump())
        session.add(provider_schema)
        await session.commit()
        await session.refresh(provider_schema)
        return provider_schema
