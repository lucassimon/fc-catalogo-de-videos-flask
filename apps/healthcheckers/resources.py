from flask import jsonify, request

from flask_restful import Resource
from flask_apispec import marshal_with
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields

from apps.logging import make_logger


logger = make_logger()


class ReadinessResponseSchema(Schema):
    message = fields.Str(default="ok")


class LivenessResponseSchema(Schema):
    message = fields.Str(default="ok")


class HealthCheckReadiness(MethodResource, Resource):
    @marshal_with(ReadinessResponseSchema)
    def get(self):
        user_agent = request.headers.get("HTTP_USER_AGENT", "UNKNOWN")
        peer_ip = request.remote_addr
        logger.info("apps.healthcheckers.resources.readiness")
        logger.info(
            "apps.healthcheckers.resources.readiness",
            extra={"props": {"extra_property": "extra_value"}},
        )
        special = "bla"
        logger.info(f"This message, though, is logged to the file! {special}")
        logger.info(
            f"{__name__}.readiness",
            extra={"user_agent": user_agent, "peer_ip": peer_ip},
        )

        return jsonify(
            {
                "message": "ok",
            }
        )


class HealthCheckLiveness(MethodResource, Resource):
    @marshal_with(LivenessResponseSchema)
    def get(self):
        return jsonify(
            {
                "message": "ok",
            }
        )
