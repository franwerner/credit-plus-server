from services.providers.insert import insert_provider
from models.provider.schema import ProviderInsert
from utils.app_response import AppSuccessResponse


async def create_provider(provider: ProviderInsert):
    res = await insert_provider(provider)

    return AppSuccessResponse(
        http_status=201,
        data=res,
        message="Proveedor creado con éxito",
    ).to_response()
