import typing as t
from flask import Flask, jsonify
from flask import json

from flask_restful import Api
import werkzeug

# Apps
from apps.messages import Messages
from apps.healthcheckers.routes import bp as bp_healthcheck
from apps.home.routes import bp as bp_home
from apps.categories.routes import bp as bp_categories


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


def handle_bad_request(e):
    resp = jsonify({"status": 400, "message": "Bad"})
    resp.status_code = 400
    return resp


def adding_xdev_header(response):
    response.headers["X-DEV"] = "Created with love."
    return response


# @app.errorhandler(DatabaseError)
# def special_exception_handler(error):
#     return "Database connection failed", 500


class InsufficientStorage(werkzeug.exceptions.HTTPException):
    code = 507
    description = "Not enough storage space."


def handle_exception(e):
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


def configure_api(app: Flask):

    app.register_blueprint(bp_healthcheck)
    app.register_blueprint(bp_home)
    app.register_blueprint(bp_categories)

    app.register_error_handler(InsufficientStorage, handle_exception)
    app.register_error_handler(werkzeug.exceptions.HTTPException, handle_exception)
    app.after_request(adding_xdev_header)

    api.init_app(app)
