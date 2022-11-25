from flask import request
from dataclasses import asdict

from flask_restful import Resource
from flask_apispec import marshal_with
from flask_apispec.views import MethodResource

from apps.responses import Response
from apps.messages import Messages
from apps.categories.commands import CreateCategoryCommand, GetCategoryCommand
from apps.categories.schemas import CreateCategorySchema


class CategoryPageList(MethodResource, Resource):
    def get(self, *args, **kwargs):
        pass


class CategoriesResource(MethodResource, Resource):
    @marshal_with(CreateCategorySchema)
    def post(self, *args, **kwargs):
        payload = request.get_json() or None
        output = CreateCategoryCommand.run(payload, *args, **kwargs)
        return Response("categories").ok(
            message=Messages.RESOURCE_CREATED.value.format("Categories"),
            data=asdict(output),
        )


class CategoryResource(MethodResource, Resource):
    def get(self, uuid: str, *args, **kwargs):
        output = GetCategoryCommand.run(uuid, *args, **kwargs)
        return Response("categories").ok(
            message=Messages.RESOURCE_FETCHED.value.format("Categories"),
            data=asdict(output),
        )

    def put(self, uuid: str, *args, **kwargs):
        pass

    def delete(self, uuid: str, *args, **kwargs):
        pass
