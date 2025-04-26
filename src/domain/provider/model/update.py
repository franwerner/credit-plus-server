from sqlmodel import select
from .schema import ProviderUpdate, Provider
from config.database import get_db_session


async def model_update_provider(provider_id: int, provider_data: ProviderUpdate):
    async with get_db_session() as _, _ as session:
        statement = select(Provider).where(Provider.provider_id == provider_id)
        update_data = provider_data.model_dump(exclude_unset=True)
        provider = (await session.exec(statement)).one()
        for key, value in update_data.items():
            setattr(provider, key, value)
        await session.commit()
        await session.refresh(provider)
        return provider
