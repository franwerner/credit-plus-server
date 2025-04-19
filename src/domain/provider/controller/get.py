from services.providers.select import select_providers, select_provider
from utils.app_response import AppSuccessResponse


async def get_providers(name_lastname: str = None, page: int = 0):
    res = await select_providers(page=page, name_lastname=name_lastname)
    return AppSuccessResponse(
        http_status=200,
        message="Proveedores obtenidos correctamente.",
        data=res,
    ).to_response()


async def get_provider(provider_id: int):
    res = await select_provider(provider_id)
    return AppSuccessResponse(
        http_status=200,
        message="Proveedor obtenido correctamente.",
        data=res,
    ).to_response()
