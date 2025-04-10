from config.database_config import Session
from models.providers.schema import Providers
from sqlalchemy import select


def select_providers():
    return Session().execute(
        select(Providers)
    ).scalars().all()


def select_provider_by_id(provider_id: int):
    return Session().execute(
        select(Providers).where(Providers.provider_id == provider_id)
    ).scalars().first()
