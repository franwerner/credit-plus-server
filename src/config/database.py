from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from .env import config
engine = create_async_engine(
    config.get("DATABASE_URL"),
    echo=True,
)


def db_session():
    return AsyncSession(engine)
