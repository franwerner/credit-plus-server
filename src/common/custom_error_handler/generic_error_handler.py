from fastapi import Request

from common.utils.app_response import AppErrorResponse


async def generic_error_handler(request: Request, exc: AppErrorResponse):
    return exc.to_response()
