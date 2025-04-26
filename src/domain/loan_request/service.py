from .model.get import get_loan_request, get_loan_requests
from common.utils.app_response import AppErrorResponse


class LoanRequestService:
    @staticmethod
    async def get_loan_request(loan_request_id: int):
        res = await get_loan_request(loan_request_id)
        if not res:
            AppErrorResponse(
                message="No se encontre ningun prestamo",
                http_status=404
            )
            return res

    @staticmethod
    async def get_loan_requests_by_client(page: int, client_id: int):
        res = await get_loan_requests(page, client_id)
        if not res:
            AppErrorResponse(
                message="No se encontraron prestamos asociados al cliente.",
                http_status=404,
            )
        return res
# Definir todos los filtros no necesarios en un objecto y los obligatorios como parametros.
