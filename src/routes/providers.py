from fastapi import APIRouter
from models.providers.select import select_provider_by_id, select_providers
from models.providers.schema import Providers
from models.providers.insert import insert_provider

router = APIRouter(prefix="/providers", tags=["providers"])


@router.get("/")
def get_providers():
    return select_providers()


@router.get("/{provider_id}")
def get_provider_by_id(provider_id: int):
    return select_provider_by_id(provider_id)


@router.post("/")
def post_provider(provider: Providers):
    insert_provider(provider)
    return "Provider created successfully"
