from fastapi.responses import JSONResponse
from fastapi import Request


async def all_exception_handler(request: Request, exc: Exception):  # pylint: disable=unused-argument
    return JSONResponse(
        status_code=500,
        content={
            "message": "Error interno inesperado",
            "code": "INTERNAL_ERROR"
        }
    )
