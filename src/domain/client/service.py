from common.utils.app_response import AppErrorResponse
from domain.client.model.schema import Client, ClientUpdate
from domain.client.model import update, get, create, delete


class ClientService:
    @staticmethod
    async def create_client(data: Client):
        return await create.model_create_client(data)

    @staticmethod
    async def update_client(client_id: int, data: ClientUpdate):
        return await update.model_update_client(client_id, data)

    @staticmethod
    async def delete_client(client_id: int):
        return await delete.model_delete_client(client_id)

    @staticmethod
    async def get_client(client_id: int):
        res = await get.model_get_client(client_id)
        if not res:
            raise AppErrorResponse(
                message="No se encontro el ciente.",
                http_status=404,
                code="CLIENT_NOT_FOUND"
            )
        return res

    @staticmethod
    async def get_clients_by_provider(page: int, provider_id: int, name_lastname: str = None):
        res = await get.model_get_clients(page, name_lastname, provider_id)
        if not res:
            raise AppErrorResponse(
                message="No se encontraron clientes.",
                http_status=404,
                code="CLIENTS_NOT_FOUND"
            )
        return res
