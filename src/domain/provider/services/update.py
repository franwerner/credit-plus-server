from domain.provider.model.update import model_update_provider
from domain.provider.model.schema import ProviderUpdate


async def service_update_provider(provider_data: ProviderUpdate, provider_id: int):
    return await model_update_provider(provider_data, provider_id)
