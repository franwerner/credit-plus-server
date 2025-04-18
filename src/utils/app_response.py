from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


class AppSuccessResponse():
    def __init__(self, message: str = "success", http_status: int = 202, data: any = None):
        self.message = message
        self.data = data
        self.http_status = http_status

    def to_response(self):
        return JSONResponse(
            content={
                "message": self.message,
                "data": jsonable_encoder(self.data)
            },
            status_code=self.http_status
        )


class AppErrorResponse(Exception, AppSuccessResponse):
    def __init__(self, message: str = "failed", code: str = "", http_status: int = 500, data: any = None):
        Exception.__init__(self, message)
        AppSuccessResponse.__init__(self, message, http_status, data)
        self.code = code

    def to_response(self):
        return JSONResponse(
            content={
                "message": self.message,
                "data": self.data,
                "code": self.code
            },
            status_code=self.http_status
        )
