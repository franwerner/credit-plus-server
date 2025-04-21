from .schema import Client
from common.utils.db_error_handler import DBErrorHandler
from sqlmodel import select
from sqlalchemy.exc import NoResultFound

error_message = {
    NoResultFound: "El cliente que intentas eliminar ya se encuentra eliminado."
}


async def model_delete_client(client_id: int):
    async with DBErrorHandler(error_message) as _, _ as session:
        query = select(Client).where(Client.client_id == client_id)
        client = (await session.exec(query)).one()
        await session.delete(client)
        await session.commit()
