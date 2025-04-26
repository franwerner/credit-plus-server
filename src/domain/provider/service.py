from domain.provider.model import create, get, update, delete
from common.utils.app_response import AppErrorResponse
from domain.provider.model.schema import Provider, ProviderUpdate


class ProviderService:
    @staticmethod
    async def create_provider(data: Provider):
        return await create.model_create_provider(data)

    @staticmethod
    async def update_provider(provider_id: int, data: ProviderUpdate):
        return await update.model_update_provider(provider_id, data)

    @staticmethod
    async def delete_provider(provider_id: int):
        await delete.model_delete_provider(provider_id)

    @staticmethod
    async def get_provider(provider_id: int):
        res = await get.model_get_provider(provider_id)
        if not res:
            raise AppErrorResponse(
                http_status=404,
                message="El Proveedor con la ID:{} no encontrado".format(provider_id),
                code="PROVIDER_NOT_FOUND"
            )
        return res

    @staticmethod
    async def get_providers(page: int = 0, name_lastname: str = None):
        res = await get.model_get_providers(page, name_lastname)
        if not res:
            raise AppErrorResponse(
                http_status=404,
                message="Proveedores no encontrados",
                code="PROVIDERS_NOT_FOUND"
            )
        return res
