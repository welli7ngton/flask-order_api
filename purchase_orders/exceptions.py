from werkzeug.exceptions import HTTPException


class MaxQuantityException(HTTPException):
    code = 400


class MinQuantityException(HTTPException):
    code = 400
