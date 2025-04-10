from fastapi import APIRouter
from models.providers.select import select_providers, select_provider_by_id
router = APIRouter(prefix="/providers", tags=["providers"])


@router.get("/")
def get_providers():
    return select_providers()


@router.get("/{provider_id}")
def get_provider_by_id(provider_id: int):
    return select_provider_by_id(provider_id)
