from sqlmodel import select, or_
from config.database import db_session
from models.provider.schema import Provider
from utils.app_response import AppErrorResponse


async def select_providers(page: int = None, name_lastname: int = None):
    page_size = 4
    query = select(Provider).limit(page_size)

    if page is not None:
        query = query.offset(page * page_size)

    if name_lastname is not None:
        query = query.where(
            or_(
                Provider.name == name_lastname,
                Provider.lastname.like(name_lastname + '%')
            )
        )

    res = (await db_session().exec(query)).all()
    if not res:
        raise AppErrorResponse(
            http_status=404,
            message="Proveedores no encontrados",
            code="PROVIDERS_NOT_FOUND"
        )
    return res


async def select_provider(provider_id: int):
    res = (await db_session().exec(
        select(Provider).where(Provider.provider_id == provider_id)
    )).first()

    if not res:
        raise AppErrorResponse(
            http_status=404,
            message="Proveedor no encontrado",
            code="PROVIDER_NOT_FOUND"
        )
    return res
