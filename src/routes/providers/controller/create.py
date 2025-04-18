from services.providers.insert import insert_provider
from models.provider import ProviderInsert


async def create_provider(provider: ProviderInsert):
    await insert_provider(provider)
    return {"message": "Provider created successfully"}
