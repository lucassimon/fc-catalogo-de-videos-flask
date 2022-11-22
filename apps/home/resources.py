from flask import jsonify

from flask_restful import Resource
from flask_apispec import marshal_with
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields

from apps.logging import make_logger


logger = make_logger()


class HomeResponseSchema(Schema):
    hello = fields.Str(default="world by apps")


class HomeResource(MethodResource, Resource):
    @marshal_with(HomeResponseSchema)
    def get(self):
        logger.info("apps.home.resources", hello="hello world")
        return jsonify({"hello": "world by apps"})
