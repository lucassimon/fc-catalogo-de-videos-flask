from typing import List

from sqlalchemy.orm.session import Session
from sqlalchemy.exc import SQLAlchemyError, DatabaseError, NoResultFound

from kernel_catalogo_videos.core.domain.unique_entity_id import UniqueEntityId
from kernel_catalogo_videos.categories.domain.repositories import CategoryRepository
from kernel_catalogo_videos.categories.domain.entities import Category as CategoryEntity

from apps.categories.models import Category as CategoryModel
from apps.categories.mapper import CategoryModelMapper
from apps.database import db
from apps.exceptions import OperationDBError


class SQLAlchemyCategoryRepository(CategoryRepository):
    session: Session = db.session

    def insert(self, entity: CategoryEntity) -> None:
        try:
            model: CategoryModel = CategoryModelMapper.to_model(entity)
            self.session.add(model)
            self.session.commit()

        except (SQLAlchemyError, DatabaseError) as exc:
            self.session.rollback()
            raise OperationDBError(exc=exc, entity=entity, operation="Create category")

        except Exception:
            raise

        finally:
            self.session.close()

    def find_by_id(self, entity_id: str | UniqueEntityId) -> CategoryEntity:
        try:
            model: CategoryModel = self.session\
                .query(CategoryModel)\
                .filter_by(id=entity_id)\
                .one()
            entity: CategoryEntity = CategoryModelMapper.to_entity(model)

            return entity
        except NoResultFound as exc:
            raise OperationDBError(
                exc=exc,
                code=404,
                operation="Get category",
                input_params={"id": entity_id},
            )

        except (SQLAlchemyError, DatabaseError) as exc:
            self.session.rollback()
            raise OperationDBError(exc=exc, entity=None, operation="Get category")

        finally:
            self.session.close()

    def find_all(self) -> List[CategoryEntity]:
        pass

    def update(self, entity: CategoryEntity) -> None:
        pass

    def delete(self, entity_id: str | UniqueEntityId) -> None:
        pass

    def _get(self, entity_id: str) -> CategoryModel:
        pass

    def search(
        self, input_params: CategoryRepository.SearchParams
    ) -> CategoryRepository.SearchResult:
        pass
