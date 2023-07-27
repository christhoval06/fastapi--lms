"""Model logic for the generics domain."""

from typing import TypeVar, Generic

from bson import ObjectId
from structlog import get_logger

from lms.api.v1 import fields
from lms.domain.repositories import generic
from lms.utils.mongo import create_query

logger = get_logger(__name__)

TOut = TypeVar('TOut')
TCreate = TypeVar('TCreate')
TUpdate = TypeVar('TUpdate')


class GenericService(Generic[TOut, TCreate, TUpdate]):
    """Orchestrator for the generics domain.
    Contains the business logic around the generics model operations.
    """

    def __init__(self, repository: generic.Repository) -> None:
        self.repository = repository
        self.table = self.repository.table
        self.schema = self.repository.schema

    async def create(self, data_object: TCreate, **kwargs) -> TOut:
        """Create a model.
        Args:
            data_object (TCreate): input data.
        Returns:
            TOut: representation of the created model.
        """
        logger.info(f"Creating {self.repository.table.__name__}", data=data_object)
        item = await self.repository.create(data_object, **kwargs)
        logger.info(f"Created {self.repository.table.__name__}", entry=item)
        return item

    async def get_by_id(self, pk: ObjectId) -> TOut:
        """Get a model by its ID.
        Args:
            pk (ObjectId): model ID.
        Returns:
            TOut: representation of the model.
        """
        logger.info(f"Getting {self.repository.table.__name__}", id=pk)
        item = await self.repository.get_by_id(pk)
        logger.info(f"Got {self.repository.table.__name__} by ID", entry=item)
        return item

    async def collect(self, **filters) -> list[TOut]:
        """Collect all models.
        Returns:
            list[TOut]: list of model.
        """
        logger.info(f"Collecting {self.repository.table.__name__}")
        items = await self.repository.collect(**filters)
        logger.info(f"Collected {self.repository.table.__name__}", qty=len(items))
        return items

    async def paginate(self, page: int = 1, limit: int = 10, **filters) -> fields.ModelOutPaginate[TOut]:
        """
        :param page:
        :param limit:
        :param filters:
        :return:
        """
        query = create_query(filters, self.table)

        count = await self.table.find(query).count()

        search = [
            self.schema.from_orm(entry)
            async for entry in self.table.find(query, skip=limit * (page - 1),
                                               limit=limit)
        ]

        has_next = limit * (page + 1) <= count

        return fields.ModelOutPaginate[TOut](
            total=count,
            page=page,
            limit=limit,
            has_next=has_next,
            data=search)

    async def delete(self, pk: ObjectId) -> None:
        """Delete a model.
        Args:
            pk (ObjectId): model ID.
        """
        logger.info(f"Deleting {self.repository.table.__name__}", id=pk)
        await self.repository.delete(pk)
        logger.info(f"Deleted {self.repository.table.__name__}", id=pk)

    async def update(self, pk: ObjectId, data_object: TUpdate) -> TOut:
        """Update a model.
        Args:
            pk (ObjectId): model ID.
            data_object (TUpdate): input data.
        Returns:
            TOut: updated model.
        """
        logger.info(f"Updating {self.repository.table.__name__}", id=pk, data=data_object)
        item = await self.repository.update(pk, data_object)
        logger.info(f"Updated {self.repository.table.__name__}", entry=item)
        return item

    async def update_many(self, ids: list[ObjectId], data_object: TUpdate) -> list[TOut]:
        """Update many models.
        Args:
            ids (list[ObjectId]): list of models IDs.
            data_object (TUpdate): input data.
        Returns:
            list[TOut]: list of updated model.
        """
        logger.info(f"Updating {self.repository.table.__name__}", ids=ids, data=data_object)
        items = await self.repository.update_many(ids, data_object)
        logger.info(f"Updated {self.repository.table.__name__}", qty=len(items))
        return items
