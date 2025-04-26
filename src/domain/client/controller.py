from domain.client.model.schema import ClientUpdate, Client
from .service import ClientService
from common.utils.app_response import AppSuccessResponse


class ClientController:
    @staticmethod
    async def update_client(client_id: int, data: ClientUpdate):
        data = await ClientService.update_client(client_id, data)
        return AppSuccessResponse(
            data=data,
        ).to_response()

    @staticmethod
    async def create_client(data: Client):
        res = await ClientService.create_client(data)
        return AppSuccessResponse(
            data=res,
            http_status=201
        ).to_response()

    @staticmethod
    async def delete_client(client_id: int):
        await ClientService.delete_client(client_id)
        return AppSuccessResponse(
            message="Cliente {} eliminado".format(client_id)
        ).to_response()

    @staticmethod
    async def get_clients(page: int = 0, name_lastname: str = None, provider_id: int = None):
        res = await ClientService.get_clients_by_provider(page, provider_id, name_lastname)
        return AppSuccessResponse(
            data=res,
        ).to_response()

    @staticmethod
    async def get_client(client_id: int):
        res = await ClientService.get_client(client_id)
        return AppSuccessResponse(
            data=res,
        ).to_response()
