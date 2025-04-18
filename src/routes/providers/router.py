from fastapi import APIRouter
from models.provider import ProviderInsert
from .controller.get import get_provider, get_providers
from .controller.create import create_provider
from .controller.remove import remove_provider
router = APIRouter(prefix="/providers", tags=["providers"])


@router.get("/")
async def gets(name_lastname: str = None, page: int = 0):
    return await get_providers(name_lastname=name_lastname, page=page)


@router.get("/{provider_id}")
async def get(provider_id: int):
    return await get_provider(provider_id=provider_id)


@router.post("/")
async def post(provider: ProviderInsert):
    return await create_provider(provider)


@router.delete("/{provider_id}")
async def delete(provider_id: int):
    return await remove_provider(provider_id=provider_id)
