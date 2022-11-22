from flask import Blueprint
from flask_restful import Api
from .resources import HealthCheckLiveness, HealthCheckReadiness

bp = Blueprint(name="healthcheck", import_name=__name__)
api_healthcheck = Api(bp)
api_healthcheck.add_resource(HealthCheckLiveness, "/health-check/liveness")
api_healthcheck.add_resource(HealthCheckReadiness, "/health-check/readiness")