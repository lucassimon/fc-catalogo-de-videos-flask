from flask import Flask, jsonify
from flask import json
from http import HTTPStatus


from flask_restful import Api
from werkzeug.exceptions import HTTPException
from marshmallow import ValidationError

# Apps
from apps.messages import Messages
from apps.healthcheckers.routes import bp as bp_healthcheck
from apps.home.routes import bp as bp_home
from apps.categories.routes import bp as bp_categories
from apps.exceptions import (
    InsufficientStorage,
    InvalidDataException,
    OperationDBError,
)

_API_ERRORS = {
    "UserAlreadyExistsError": {"status": 409, "message": Messages.ALREADY_EXISTS.value},
    "ResourceDoesNotExist": {
        "status": 410,
        "message": Messages.RESOURCE_DOES_NOT_EXIST.value,
    },
    "MethodNotAllowed": {"status": 405, "message": Messages.RESOURCE_NOT_ALLOWED.value},
    "NotFound": {"status": 404, "message": Messages.RESOURCE_NOT_FOUND.value},
    "BadRequest": {"status": 400, "message": Messages.RESOURCE_BAD_REQUEST.value},
    "InternalServerError": {
        "status": 500,
        "message": Messages.RESOURCE_BAD_REQUEST.value,
    },
}

api = Api(
    catch_all_404s=True,
    errors=_API_ERRORS,
)


def adding_xdev_header(response):
    response.headers["X-DEV"] = "Created with love."
    return response


# @app.errorhandler(DatabaseError)
# def special_exception_handler(error):
#     return "Database connection failed", 500


def handle_database_error(exc:OperationDBError):
    http = HTTPStatus(exc.code)
    data = {
        "code": exc.code,
        "name": http.phrase,
        "description": http.description,
        "operation": exc.operation,
        "messsage": exc.message,
        "exception": exc.__class__.__name__
    }

    if hasattr(exc, "entity") and exc.entity is not None:
        data.update({"entity": exc.entity.to_dict()})

    if hasattr(exc, "extra") and exc.extra is not None:
        data.update({"extra": exc.extra})

    resp = jsonify(data)

    resp.status_code = http
    return resp


def handle_validation_error(exc:ValidationError):
    resp = jsonify(
        {
            "code": 422,
            "name": HTTPStatus.UNPROCESSABLE_ENTITY.phrase,
            "description": HTTPStatus.UNPROCESSABLE_ENTITY.description,
            "errors": exc.messages,
        }
    )
    resp.status_code = HTTPStatus.UNPROCESSABLE_ENTITY
    return resp


def handle_http_exception(e: HTTPException):
    """Return JSON instead of HTML for HTTP errors."""

    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON

    response.data = json.dumps(
        {
            "code": e.code,
            "name": e.name,
            "description": e.description,
        }
    )
    response.content_type = "application/json"
    return response


def handle_exception(exc: BaseException):
    resp = jsonify(
        {
            "code": 500,
            "name": HTTPStatus.INTERNAL_SERVER_ERROR.phrase,
            "description": HTTPStatus.INTERNAL_SERVER_ERROR.description,
            "errors": exc.args[0],
            "class": exc.__class__.__name__
        }
    )
    resp.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    return resp



def configure_api(app: Flask):

    app.register_blueprint(bp_healthcheck)
    app.register_blueprint(bp_home)
    app.register_blueprint(bp_categories)

    app.register_error_handler(InsufficientStorage, handle_http_exception)
    app.register_error_handler(HTTPException, handle_http_exception)
    app.register_error_handler(ValidationError, handle_validation_error)
    app.register_error_handler(InvalidDataException, handle_validation_error)
    app.register_error_handler(OperationDBError, handle_database_error)
    app.register_error_handler(Exception, handle_exception)
    app.after_request(adding_xdev_header)

    api.init_app(app)
