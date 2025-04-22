from .model.schema import ProviderUpdate, ProviderInsert
from .service import ProviderService
from common.utils.app_response import AppSuccessResponse


class ProviderController:

    @staticmethod
    async def get_provider(provider_id: int):
        res = await ProviderService.get_provider(provider_id)
        return AppSuccessResponse(
            data=res,
        ).to_response()

    @staticmethod
    async def get_providers(page: int = 0, name_lastname: str = None):
        res = await ProviderService.get_providers(page, name_lastname)
        return AppSuccessResponse(
            data=res,
        ).to_response()

    @staticmethod
    async def create_provider(data: ProviderInsert):
        res = await ProviderService.create_provider(data)
        return AppSuccessResponse(
            data=res,
            http_status=201
        ).to_response()

    @staticmethod
    async def update_provider(provider_id: int, data: ProviderUpdate):
        res = await ProviderService.update_provider(provider_id, data)
        return AppSuccessResponse(
            data=res,
        ).to_response()

    @staticmethod
    async def delete_provider(provider_id: int):
        res = await ProviderService.delete_provider(provider_id)
        return AppSuccessResponse(
            message="Proveedor {} eliminado correctamente".format(provider_id)
        ).to_response()
