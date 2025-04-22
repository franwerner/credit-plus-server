from .schema import Provider
from sqlmodel import select, or_
from common.utils.db_error_handler import DBErrorHandler


async def model_get_providers(page: int = 0, name_lastname: int = None):
    page_limit = 15
    query = (
        select(Provider)
        .limit(page_limit)
        .offset(page * page_limit)
    )

    if name_lastname is not None:
        query = query.where(
            or_(
                Provider.name == name_lastname,
                Provider.lastname.like(name_lastname + '%')
            )
        )
    async with DBErrorHandler() as session:
        return (await session.exec(query)).all()


async def model_get_provider(provider_id: int):
    async with DBErrorHandler() as session:
        return (await session.exec(
            select(Provider).where(Provider.provider_id == provider_id)
        )).first()
