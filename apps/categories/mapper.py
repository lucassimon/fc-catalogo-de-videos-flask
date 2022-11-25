from kernel_catalogo_videos.core.domain.unique_entity_id import UniqueEntityId
from kernel_catalogo_videos.categories.domain.entities import Category as CategoryEntity

from apps.categories.models import Category as CategoryModel

class CategoryModelMapper:

    @staticmethod
    def to_entity(model: CategoryModel) -> CategoryEntity:
        return CategoryEntity(
            unique_entity_id=UniqueEntityId(str(model.id)),
            title=model.title,
            slug=model.slug,
            description=model.description,
            status=model.status,
            is_deleted=model.is_deleted,
            created_at=model.created_at,
        )


    @staticmethod
    def to_model(entity: CategoryEntity) -> CategoryModel:
        return CategoryModel(**entity.to_dict())
