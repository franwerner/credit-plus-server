from services.providers.select import select_providers, select_provider


async def get_providers(name_lastname: str = None, page: int = 0):
    return await select_providers(page=page, name_lastname=name_lastname)


async def get_provider(provider_id: int):
    return await select_provider(provider_id)
