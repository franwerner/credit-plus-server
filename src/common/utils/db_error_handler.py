from typing import TypedDict
from sqlalchemy.exc import OperationalError, IntegrityError, NoResultFound
from config.database import db_session
from common.utils.app_response import AppErrorResponse


class DBConfigError(TypedDict):
    http_status: int
    message: str
    code: str


generic_message = {
    "http_status": 500,
    "message": "Error desconocido en la base de datos",
    "code": "DB_ERROR"
}

errors_messages: dict[str, DBConfigError] = {
    OperationalError: {
        "http_status": 500,
        "message": "Error en la base de datos",
        "code": "OPERATIONAL_ERROR"
    },
    IntegrityError: {
        "http_status": 400,
        "message": "Error de integridad de datos, violación de restricciones",
        "code": "INTEGRITY_ERROR"
    },
    NoResultFound: {
        "http_status": 403,
        "message": "No se encontraron resultados",
        "code": "NO_RESULT_FOUND"
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
        print(exc_type, exc_value)
        if not exc_type:
            return

        get_error_config = (
            errors_messages.get(exc_type) or
            generic_message
        )

        message = (
            self.extend_messages.get(exc_type) or
            get_error_config.get("message")
        )

        raise AppErrorResponse(
            http_status=get_error_config.get("http_status"),
            message=message,
            code=get_error_config.get("code")
        )
