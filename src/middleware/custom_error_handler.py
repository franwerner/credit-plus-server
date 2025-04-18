from fastapi import Request
from utils.app_response import AppErrorResponse


def custom_error_handler(app):
    @app.exception_handler(AppErrorResponse)
    async def internal(request: Request, exc: AppErrorResponse):  # pylint: disable=unused-argument
        return exc.to_response()
