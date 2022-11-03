"""Model logic for the borrowers domain."""

import uuid

from structlog import get_logger
from bson import ObjectId

from lms.api.v1 import fields
from lms.domain.repositories import generic

logger = get_logger(__name__)


class BorrowerService:
    """Orchestrator for the borrowers domain.
    Contains the business logic around the borrowers model operations.
    """

    def __init__(self, repository: generic.Repository) -> None:
        self.repository = repository

    async def create(
            self,
            data_object: fields.BorrowerCreate,
    ) -> fields.BorrowerOut:
        """Create a new borrower.
        Args:
            data_object (BorrowerCreate): input data.
        Returns:
            BorrowerOut: representation of the created borrower.
        """
        logger.info("Creating borrower", data=data_object)
        logger.info("Creating borrower", data=data_object)
        borrower = await self.repository.create(data_object)
        logger.info("Created borrower", entry=borrower)
        return borrower

    async def get_by_id(self, pk: ObjectId) -> fields.BorrowerOut:
        """Get a borrower by its ID.
        Args:
            pk (ObjectId): borrower ID.
        Returns:
            BorrowerOut: representation of the borrower.
        """
        logger.info("Getting borrower", id=pk)
        borrower = await self.repository.get_by_id(pk)
        logger.info("Got borrower by ID", entry=borrower)
        return borrower

    async def collect(self) -> list[fields.BorrowerOut]:
        """Collect all borrowers.
        Returns:
            list[BorrowerOut]: list of borrowers.
        """
        logger.info("Collecting borrowers")
        borrowers = await self.repository.collect()
        logger.info("Collected borrowers", qty=len(borrowers))
        return borrowers

    async def delete(self, pk: ObjectId) -> None:
        """Delete a borrower.
        Args:
            pk (ObjectId): borrower ID.
        """
        logger.info("Deleting borrower", id=pk)
        await self.repository.delete(pk)
        logger.info("Deleted borrower", id=pk)

    async def update(
            self,
            pk: ObjectId,
            data_object: fields.BorrowerUpdate,
    ) -> fields.BorrowerOut:
        """Update a borrower.
        Args:
            pk (ObjectId): borrower ID.
            data_object (BorrowerUpdate): input data.
        Returns:
            BorrowerOut: updated borrower.
        """
        logger.info("Updating borrower", id=pk, data=data_object)
        borrower = await self.repository.update(pk, data_object)
        logger.info("Updated borrower", entry=borrower)
        return borrower

    async def update_many(
            self,
            ids: list[ObjectId],
            data_object: fields.BorrowerUpdate,
    ) -> list[fields.BorrowerOut]:
        """Update many borrowers.
        Args:
            ids (list[ObjectId]): list of borrower IDs.
            data_object (BorrowerUpdate): input data.
        Returns:
            list[BorrowerOut]: list of updated borrowers.
        """
        logger.info("Updating borrowers", ids=ids, data=data_object)
        borrowers = await self.repository.update_many(ids, data_object)
        logger.info("Updated borrowers", qty=len(borrowers))
        return borrowers
