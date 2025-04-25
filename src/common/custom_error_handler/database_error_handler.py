from fastapi import Request
from sqlalchemy.exc import OperationalError, IntegrityError, NoResultFound, DatabaseError
from typing import TypedDict
from common.utils.app_response import AppErrorResponse


class DBConfigError(TypedDict):
    http_status: int
    message: str


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


async def database_error_handler(request: Request, exc: DatabaseError):
    error_message = errors_messages.get(type(exc)) or generic_message
    return AppErrorResponse(
        message=error_message.get("message"),
        code="DATABASE_ERROR",
        http_status=error_message.get("http_status"),
    ).to_response()
