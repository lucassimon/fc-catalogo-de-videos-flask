from typing import List

from kernel_catalogo_videos.core.domain.unique_entity_id import UniqueEntityId
from kernel_catalogo_videos.categories.domain.repositories import CategoryRepository
from kernel_catalogo_videos.categories.domain.entities import Category as CategoryEntity

from apps.categories.models import Category as CategoryModel


class SQLAlchemyCategoryRepository(CategoryRepository):

    def insert(self, entity: CategoryEntity) -> None:
        pass

    def find_by_id(self, entity_id: str | UniqueEntityId) -> CategoryEntity:
        pass

    def find_all(self) -> List[CategoryEntity]:
        pass

    def update(self, entity: CategoryEntity) -> None:
        pass

    def delete(self, entity_id: str | UniqueEntityId) -> None:
        pass

    def _get(self, entity_id: str) -> CategoryModel:
        pass

    def search(self, input_params: CategoryRepository.SearchParams) -> CategoryRepository.SearchResult:
        pass