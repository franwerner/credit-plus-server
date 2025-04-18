from json import loads
from starlette.concurrency import iterate_in_threadpool
from fastapi import Request
from utils.app_response import AppErrorResponse
from config.env import config

# Solo se ejecuta si el entorno es de desarrollo


def verify_response(app):
    if config.get("MODE") != "DEV":
        return

    @app.middleware("http")
    async def internal(request: Request, call_next):
        response = await call_next(request)
        if request.url.path.startswith(("/docs", "/redoc", "/openapi")):
            return response

        response_body = [chunk async for chunk in response.body_iterator]
        response.body_iterator = iterate_in_threadpool(iter(response_body))
        try:
            # Construir la instacia para ver si cumple con el contrato de interfaz.
            AppErrorResponse(**loads(response_body[0].decode()))
        except TypeError:
            return AppErrorResponse(
                code="INVALID_RESPONSE",
                message="Estructura de la respuesta invalida."
            ).to_response()

        return response
