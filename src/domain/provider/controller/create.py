from domain.provider.model.schema import ProviderInsert
from common.utils.app_response import AppSuccessResponse
from domain.provider.services.create import service_create_provider


async def controller_create_provider(provider: ProviderInsert):
    res = await service_create_provider(provider)
    return AppSuccessResponse(
        http_status=201,
        data=res,
        message="Proveedor creado con éxito",
    ).to_response()
