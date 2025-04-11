from config.database_config import db_session
from .schema import Providers


def insert_provider(provider: Providers):
    with db_session() as session:
        session.add(provider)
        session.commit()
