from domain.provider.model.schema import ProviderInsert
from domain.provider.model.create import model_create_provider


async def service_create_provider(provider: ProviderInsert):
    return await model_create_provider(provider)
