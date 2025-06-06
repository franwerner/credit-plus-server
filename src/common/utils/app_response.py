from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


class AppSuccessResponse:
    def __init__(
            self,
            message: str = "success",
            http_status: int = 200,
            data: any = None
    ):
        self.message = message
        self.data = data
        self.http_status = http_status

    def to_response(self):
        content = {
            "message": self.message,
        }
        print(content)
        if self.data:
            content["data"] = jsonable_encoder(self.data)
        return JSONResponse(
            content=content,
            status_code=self.http_status
        )


class AppErrorResponse(Exception, AppSuccessResponse):
    def __init__(
            self,
            message: str = "failed",
            code: str = "",
            http_status: int = 500,
            data: any = None
    ):
        Exception.__init__(self, message)
        AppSuccessResponse.__init__(self, message, http_status, data)
        self.code = code

    def to_response(self):
        content = {
            "message": self.message,
            "code": self.code,
        }
        if self.data:
            content["data"] = self.data
        return JSONResponse(
            content=content,
            status_code=self.http_status
        )
