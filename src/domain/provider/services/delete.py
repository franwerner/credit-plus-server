from domain.provider.model.delete import model_delete_provider
from common.utils.app_response import AppErrorResponse


async def service_delete_provider(provider_id: int):
    row_count = await model_delete_provider(provider_id)
    if row_count == 0:
        raise AppErrorResponse(
            http_status=404,
            message="El proveedor que intentas eliminar,no se encuentra.",
            code="PROVIDER_NOT_FOUND"
        )
