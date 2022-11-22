from flask import Blueprint
from flask_restful import Api
from .resources import HomeResource

bp = Blueprint(name="home", import_name=__name__)
api_healthcheck = Api(bp)
api_healthcheck.add_resource(HomeResource, "/")
