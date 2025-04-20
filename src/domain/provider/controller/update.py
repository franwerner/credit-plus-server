from domain.provider.model.schema import ProviderUpdate
from domain.provider.services.update import service_update_provider
from common.utils.app_response import AppSuccessResponse


async def controller_provider_update(provider_data: ProviderUpdate, provider_id: int):
    res = await service_update_provider(provider_data, provider_id)
    return AppSuccessResponse(
        data=res,
        http_status=200,
        message="Proveedor actualizado exitosamente."
    )
