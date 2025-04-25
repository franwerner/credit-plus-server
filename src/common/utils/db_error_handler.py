from typing import TypedDict
from sqlalchemy.exc import OperationalError, IntegrityError, NoResultFound, DatabaseError
from config.database import db_session
from common.utils.app_response import AppErrorResponse


class DBConfigError(TypedDict):
    http_status: int
    message: str
    code: str


generic_message = {
    "http_status": 500,
    "message": "Error desconocido en la base de datos",
}

errors_messages: dict[str, DBConfigError] = {
    OperationalError: {
        "http_status": 500,
        "message": "Error en la base de datos",
    },
    IntegrityError: {
        "http_status": 400,
        "message": "Error de integridad de datos, violación de restricciones",
    },
    NoResultFound: {
        "http_status": 403,
        "message": "No se encontraron resultados",
    }
}


class DBErrorHandler():
    def __init__(
            self,
            extend_messages: dict[str, str] = None
    ):
        self.extend_messages = extend_messages or {}

    async def __aenter__(self):
        return db_session()

    async def __aexit__(self, exc_type, exc_value, traceback):
        return
