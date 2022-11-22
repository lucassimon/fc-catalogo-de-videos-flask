from flask import Blueprint
from flask_restful import Api
from .resources import CategoriesResource

bp = Blueprint(name="categories", import_name=__name__, url_prefix="/api/v1")
api_healthcheck = Api(bp)
api_healthcheck.add_resource(CategoriesResource, "/categories")
