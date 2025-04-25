from fastapi import APIRouter

from domain.provider.model.schema import ProviderUpdate, Provider
from .controller import ProviderController

router = APIRouter(prefix="/providers", tags=["Providers"])


@router.get("/{provider_id}")
async def get(provider_id: int):
    return await ProviderController.get_provider(provider_id)


@router.get("/")
async def gets(name_lastname: str = None, page: int = 0):
    return await ProviderController.get_providers(page, name_lastname)


@router.post("/")
async def post(provider: Provider):
    return await ProviderController.create_provider(provider)


@router.delete("/{provider_id}")
async def delete(provider_id: int):
    return await ProviderController.delete_provider(provider_id)


@router.patch("/{provider_id}")
async def patch(provider_id: int, body: ProviderUpdate):
    return await ProviderController.update_provider(provider_id, body)
