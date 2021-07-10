import http


class TaskHTTPException(BaseException):
    def __init__(self, http_status: http.HTTPStatus, message):
        self.http_status = http_status
        self.message = message
        super().__init__(self.message)
