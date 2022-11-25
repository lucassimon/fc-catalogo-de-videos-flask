from flask import Blueprint
from flask_restful import Api
from .resources import CategoriesResource, CategoryResource

bp = Blueprint(name="categories", import_name=__name__, url_prefix="/api/v1")
api = Api(bp)
api.add_resource(CategoriesResource, "/categories")
api.add_resource(CategoryResource, "/categories/<string:uuid>")
