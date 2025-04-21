from domain.provider.model.delete import model_delete_provider


async def service_delete_provider(provider_id: int):
    return await model_delete_provider(provider_id)
