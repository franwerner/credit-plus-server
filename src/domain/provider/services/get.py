from domain.provider.model.get import model_get_provider, model_get_providers
from common.utils.app_response import AppErrorResponse


async def service_get_providers(name_lastname: str = None, page: int = 0):
    res = await model_get_providers(name_lastname=name_lastname, page=page)
    if not res:
        raise AppErrorResponse(
            http_status=404,
            message="Proveedores no encontrados",
            code="PROVIDERS_NOT_FOUND"
        )
    return res


async def service_get_provider(provider_id: int):
    res = await model_get_provider(provider_id)
    if not res:
        raise AppErrorResponse(
            http_status=404,
            message="Proveedor no encontrado",
            code="PROVIDER_NOT_FOUND"
        )
    return res
