from domain.provider.services.delete import service_delete_provider
from common.utils.app_response import AppErrorResponse


async def controller_remove_provider(provider_id: int):
    await service_delete_provider(provider_id)
    return AppErrorResponse(
        http_status=200,
        message="Proveedor eliminador correctamente.",
    ).to_response()
