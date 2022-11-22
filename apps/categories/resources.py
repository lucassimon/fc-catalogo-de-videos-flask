from flask import request

from flask_restful import Resource
from flask_apispec import marshal_with
from flask_apispec.views import MethodResource

from apps.categories.operations.create_category import create, CreateCategorySchema


class CategoryPageList(MethodResource, Resource):
    def get(self, *args, **kwargs):
        pass


class CategoriesResource(MethodResource, Resource):
    @marshal_with(CreateCategorySchema)
    def post(self, *args, **kwargs):
        payload = request.get_json() or None
        return create(payload, *args, **kwargs)


class CategoryResource(MethodResource, Resource):
    def get(self, *args, **kwargs):
        pass

    def put(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass
