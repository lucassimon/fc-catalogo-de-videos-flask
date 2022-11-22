# Python
from http import HTTPStatus
from typing import Any

# Flask
from flask import jsonify

# Apps
from apps.messages import Messages


class Response:
    def __init__(self, resource):
        if not isinstance(resource, str):
            raise ValueError(Messages.PARAM_IS_STRING.value.format("resource"))

        self.resource = resource

    def notallowed_user(self, msg: str = Messages.USER_HAS_NO_PERMISSIONS.value):
        if not isinstance(msg, str):
            raise ValueError(Messages.PARAM_IS_STRING.value.format("msg"))

        resp = jsonify({"resource": self.resource, "message": msg})
        resp.status_code = HTTPStatus.UNAUTHORIZED
        return resp

    def data_invalid(self, errors: dict, msg=Messages.INVALID_DATA.value):
        if not isinstance(errors, dict):
            raise ValueError(Messages.PARAM_IS_DICT.value.format("errors"))

        if not isinstance(msg, str):
            raise ValueError(Messages.PARAM_IS_STRING.value.format("msg"))

        resp = jsonify({"resource": self.resource, "message": msg, "errors": errors})
        resp.status_code = HTTPStatus.BAD_REQUEST
        return resp

    def does_not_exist(self, description: str):
        if not isinstance(description, str) or not description:
            raise ValueError(Messages.PARAM_IS_STRING.value.format("description"))

        resp = jsonify(
            {
                "message": Messages.DOES_NOT_EXIST.value.format(description),
                "resource": self.resource,
            }
        )
        resp.status_code = HTTPStatus.NOT_FOUND
        return resp

    def exception(self, msg: str = Messages.EXCEPTION.value, description: str = ""):
        if not isinstance(msg, str):
            raise ValueError(Messages.PARAM_IS_STRING.value.format("msg"))

        if not isinstance(description, str) or not description:
            raise ValueError(Messages.PARAM_IS_STRING.value.format("description"))

        resp = jsonify(
            {
                "message": msg,
                "resource": self.resource,
                "description": "{}".format(description),
            }
        )
        resp.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        return resp

    def already_exists(self, description: str = ""):
        if not isinstance(description, str) or not description:
            raise ValueError(Messages.PARAM_IS_STRING.value.format("description"))

        resp = jsonify(
            {
                "resource": self.resource,
                "message": Messages.ALREADY_EXISTS.value.format(description),
            }
        )
        resp.status_code = HTTPStatus.CONFLICT
        return resp

    def ok(self, message: str, status: int = HTTPStatus.OK, data: Any = None, **extras):
        if not isinstance(message, str):
            raise ValueError(Messages.PARAM_IS_STRING.value.format("message"))

        if not isinstance(status, int):
            raise ValueError(Messages.PARAM_IS_INT.value.format("status"))

        response = {"status": status, "message": message, "resource": self.resource}

        if data:
            response["data"] = data

        response.update(extras)
        resp = jsonify(response)
        resp.status_code = status
        return resp
