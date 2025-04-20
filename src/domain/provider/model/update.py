from sqlmodel import select
from .schema import ProviderUpdate, Provider
from common.utils.db_error_handler import DBErrorHandler
from sqlalchemy.exc import NoResultFound

err_messages = {
    NoResultFound: "El proveedor que intentas actualizar, no existe."
}


async def model_update_provider(provider_data: ProviderUpdate, provider_id: int):
    async with DBErrorHandler(err_messages) as _, _ as session:
        statement = select(Provider).where(Provider.provider_id == provider_id)
        update_data = provider_data.model_dump(exclude_unset=True)
        provider = (await session.exec(statement)).one()
        for key, value in update_data.items():
            setattr(provider, key, value)
        await session.commit()
        await session.refresh(provider)
        return provider
