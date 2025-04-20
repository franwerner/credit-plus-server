from common.utils.app_response import AppSuccessResponse
from domain.provider.services.get import service_get_providers, service_get_provider


async def controller_get_providers(name_lastname: str = None, page: int = 0):
    res = await service_get_providers(page=page, name_lastname=name_lastname)
    return AppSuccessResponse(
        http_status=200,
        message="Proveedores obtenidos correctamente.",
        data=res,
    ).to_response()


async def controller_get_provider(provider_id: int):
    res = await service_get_provider(provider_id)
    return AppSuccessResponse(
        http_status=200,
        message="Proveedor obtenido correctamente.",
        data=res,
    ).to_response()
