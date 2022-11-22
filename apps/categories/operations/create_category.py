from dataclasses import asdict

from marshmallow import Schema, fields, ValidationError, validate
from kernel_catalogo_videos.core.utils import ACTIVE_STATUS, INACTIVE_STATUS
from kernel_catalogo_videos.categories.application.use_cases.create.use_case import (
    CreateCategoryUseCase,
)
from kernel_catalogo_videos.categories.application.use_cases.create.input import (
    CreateCategoryInput,
)

from apps.messages import Messages
from apps.responses import Response
from apps.categories.repositories import SQLAlchemyCategoryRepository


def validate_status(value):
    if value != ACTIVE_STATUS or value != INACTIVE_STATUS:
        raise ValidationError(
            f"The status needs to be {ACTIVE_STATUS} for active or {INACTIVE_STATUS} to inactive ."
        )


class CreateCategorySchema(Schema):
    title = fields.Str(
        required=True, error_messages={"required": Messages.FIELD_REQUIRED.value}
    )
    description = fields.Str(required=False)
    status = fields.Integer(validate=validate_status)


def create(payload, *args, **kwargs):
    if payload is None:
        return Response("categories").data_invalid(
            "categories", {}, msg=Messages.NO_DATA.value
        )

    import ipdb

    ipdb.set_trace()

    try:
        data: CreateCategorySchema = CreateCategorySchema().load(payload)
        input_params = CreateCategoryInput(title=data["title"])
        if "description" in data:
            input_params.description = data["description"]

        if "status" in data:
            input_params.status = data["status"]

        repo: SQLAlchemyCategoryRepository = SQLAlchemyCategoryRepository()
        output = CreateCategoryUseCase(repo=repo).execute(input_params=input_params)
        return Response("categories").ok(
            message=Messages.RESOURCE_CREATED.value.format("Categories"),
            data=asdict(output),
        )
    except ValidationError as err:
        return Response("categories").data_invalid(errors=err)
    except Exception as exc:
        return Response("categories").exception(description=exc.__str__())
