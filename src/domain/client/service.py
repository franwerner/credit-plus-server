from common.utils.app_response import AppErrorResponse
from domain.client.model.schema import ClientInsert, ClientUpdate
from domain.client.model import update, get, create, delete


class ClientService:
    @staticmethod
    async def create_client(data: ClientInsert):
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
                message="El cliente con la ID:{} no encontrado".format(client_id),
                http_status=404,
                code="CLIENT_NOT_FOUND"
            )
        return res

    @staticmethod
    async def get_clients(page: int = 0, name_lastname: str = None, provider_id: int = None):
        res = await get.model_get_clients(page, name_lastname, provider_id)
        if not res:
            raise AppErrorResponse(
                message="No hay mas clientes",
                http_status=404,
                code="CLIENTS_NOT_FOUND"
            )
        return res
