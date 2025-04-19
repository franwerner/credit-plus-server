from sqlmodel import delete
from sqlalchemy import CursorResult
from config.database import db_session
from models.provider.schema import Provider
from utils.app_response import AppErrorResponse


async def delete_provider(provider_id: int):
    async with db_session() as session:
        query = delete(Provider).where(Provider.provider_id == provider_id)
        affects: CursorResult = await session.exec(query)
        if affects.rowcount == 0:
            raise AppErrorResponse(
                http_status=404,
                message="El proveedor que intentas eliminar,no se encuentra.",
                code="PROVIDER_NOT_FOUND"
            )
        await session.commit()
