from services.providers.delete import delete_provider
from utils.app_response import AppErrorResponse


async def remove_provider(provider_id: int):
    await delete_provider(provider_id)
    return AppErrorResponse(
        http_status=200,
        message="Proveedor eliminador correctamente.",
    ).to_response()
