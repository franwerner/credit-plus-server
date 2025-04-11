from sqlalchemy import select
from config.database_config import db_session
from .schema import Providers


def select_providers():
    return db_session().exec(
        select(Providers)
    ).scalars().all()


def select_provider_by_id(provider_id: int):
    return db_session().exec(
        select(Providers).where(Providers.provider_id == provider_id)
    ).scalars().first()
