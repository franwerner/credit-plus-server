from fastapi import APIRouter
from domain.provider.model.schema import ProviderInsert, ProviderUpdate
from domain.provider.controller.get import controller_get_provider, controller_get_providers
from domain.provider.controller.create import controller_create_provider
from domain.provider.controller.delete import controller_remove_provider
from domain.provider.controller.update import controller_provider_update

router = APIRouter(prefix="/providers", tags=["Provider"])


@router.get("/")
async def gets(name_lastname: str = None, page: int = 0):
    return await controller_get_providers(name_lastname=name_lastname, page=page)


@router.get("/{provider_id}")
async def get(provider_id: int):
    return await controller_get_provider(provider_id=provider_id)


@router.post("/")
async def post(provider: ProviderInsert):
    return await controller_create_provider(provider)


@router.delete("/{provider_id}")
async def delete(provider_id: int):
    return await controller_remove_provider(provider_id=provider_id)


@router.patch("/{provider_id}")
async def patch(provider_id: int, body: ProviderUpdate):
    return await controller_provider_update(body, provider_id)
