from fastapi import Request
from pydantic import ValidationError
from common.utils.app_response import AppErrorResponse


async def validation_error_handler(request: Request, exc: ValidationError):
    return AppErrorResponse(
        message="Error en la validacion de los datos de entrada.",
        http_status=422,
        code="VALIDATION_ERROR",
        data=exc.errors()
    ).to_response()
