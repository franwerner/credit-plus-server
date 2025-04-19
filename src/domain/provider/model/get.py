from .schema import Provider
from sqlmodel import select, or_
from config.database import db_session


async def model_get_providers(page: int = None, name_lastname: int = None):
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

    return (await db_session().exec(query)).all()


async def model_get_provider(provider_id: int):
    return (await db_session().exec(
        select(Provider).where(Provider.provider_id == provider_id)
    )).first()
