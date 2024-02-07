from werkzeug.exceptions import HTTPException


class UserAreadyExistsException(HTTPException):
    code = 400


class UserEmailOrPasswordInvalidException(HTTPException):
    code = 404
