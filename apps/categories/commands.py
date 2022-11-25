from typing import Any, Mapping
from marshmallow import ValidationError

from kernel_catalogo_videos.categories.application.use_cases.create.use_case import (
    CreateCategoryUseCase,
)
from kernel_catalogo_videos.categories.application.use_cases.create.input import (
    CreateCategoryInput,
)
from kernel_catalogo_videos.categories.application.use_cases.create.output import (
    CreateCategoryOutput,
)
from kernel_catalogo_videos.categories.application.use_cases.get.input import (
    GetCategoryInput
)
from kernel_catalogo_videos.categories.application.use_cases.get.output import (
    GetCategoryOutput
)
from kernel_catalogo_videos.categories.application.use_cases.get.use_case import (
    GetCategoryUseCase
)

from apps.exceptions import InvalidDataException
from apps.categories.repositories import SQLAlchemyCategoryRepository
from apps.categories.schemas import CreateCategorySchema

class CreateCategoryCommand:
    @staticmethod
    def save_in_database(payload: Mapping[str, Any], *args, **kwargs: dict):
        if payload is None:
            raise InvalidDataException()

        try:
            data: CreateCategorySchema = CreateCategorySchema().load(payload)
            input_params = CreateCategoryInput(title=data["title"])
            if "description" in data:
                input_params.description = data["description"]

            if "status" in data:
                input_params.status = data["status"]

            repo: SQLAlchemyCategoryRepository = SQLAlchemyCategoryRepository()
            use_case: CreateCategoryUseCase = CreateCategoryUseCase(repo=repo)
            output: CreateCategoryOutput = use_case.execute(input_params=input_params)
            return output

        except ValidationError:
            raise

        except Exception:
            raise

    @staticmethod
    def send_to_rabbitmq(output: CreateCategoryOutput):
        pass

    @staticmethod
    def run(payload: Mapping[str, Any], *args, **kwargs: dict):
        output = CreateCategoryCommand.save_in_database(payload, *args, **kwargs)

        return output

class GetCategoryCommand:

    @staticmethod
    def run(uuid: str, *args, **kwargs: dict):
        try:
            input_params = GetCategoryInput(id=uuid)
            repo: SQLAlchemyCategoryRepository = SQLAlchemyCategoryRepository()
            use_case: GetCategoryUseCase = GetCategoryUseCase(repo=repo)
            output: GetCategoryOutput = use_case.execute(input_params=input_params)
            return output
        except ValidationError:
            raise

        except Exception:
            raise
