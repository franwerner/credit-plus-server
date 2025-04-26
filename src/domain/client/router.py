from fastapi import APIRouter

from .controller import ClientController
from .model.schema import ClientUpdate, Client

router = APIRouter(prefix="/clients", tags=["Clients"])


@router.get("/{client_id}")
async def get(client_id: int):
    return await ClientController.get_client(client_id)


@router.get("/")
async def gets(page: int = 0, name_lastname: str = None, provider_id: int = None):
    return await ClientController.get_clients(page, name_lastname, provider_id)


@router.post("/")
async def post(body: Client):
    return await ClientController.create_client(body)


@router.delete("/{client_id}")
async def delete(client_id: int):
    return await ClientController.delete_client(client_id)


@router.patch("/{client_id}")
async def patch(client_id: int, body: ClientUpdate):
    return await ClientController.update_client(client_id, body)
