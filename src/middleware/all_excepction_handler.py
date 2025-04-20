from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request


def all_excepction_handler(app: FastAPI):
    @app.exception_handler(Exception)
    def internal(request: Request, exc: Exception):  # pylint: disable=unused-argument
        return JSONResponse(
            status_code=500,
            content={
                "message": "Error interno inesperado",
                "code": "INTERNAL_ERROR"
            }
        )
