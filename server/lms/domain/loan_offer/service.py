"""Model logic for the loan offer domain."""

import uuid

from structlog import get_logger
from bson import ObjectId

from lms.api.v1 import fields
from lms.domain.repositories import generic

logger = get_logger(__name__)


class LoanOfferService:
    """Orchestrator for the loan offer domain.
    Contains the business logic around the loan offer model operations.
    """

    def __init__(self, repository: generic.Repository) -> None:
        self.repository = repository

    async def create(
            self,
            data_object: fields.LoanOfferCreate,
    ) -> fields.LoanOfferOut:
        """Create a new borrower.
        Args:
            data_object (LoanOfferCreate): input data.
        Returns:
            LoanOfferOut: representation of the created loan_offer.
        """
        logger.info("Creating loan offer", data=data_object)
        logger.info("Creating loan offer", data=data_object)
        loan_offer = await self.repository.create(data_object)
        logger.info("Created loan offer", entry=loan_offer)
        return loan_offer

    async def get_by_id(self, pk: ObjectId) -> fields.LoanOfferOut:
        """Get a loan_offer by its ID.
        Args:
            pk (ObjectId): loan_offer ID.
        Returns:
            LoanOfferOut: representation of the loan_offer.
        """
        logger.info("Getting loan offer", id=pk)
        loan_offer = await self.repository.get_by_id(pk)
        logger.info("Got loan offer by ID", entry=loan_offer)
        return loan_offer

    async def collect(self) -> list[fields.LoanOfferOut]:
        """Collect all loan offer.
        Returns:
            list[LoanOfferOut]: list of loan offer.
        """
        logger.info("Collecting loan offers")
        loan_offers = await self.repository.collect()
        logger.info("Collected loan offers", qty=len(loan_offers))
        return loan_offers

    async def delete(self, pk: ObjectId) -> None:
        """Delete a loan_offer.
        Args:
            pk (ObjectId): loan_offer ID.
        """
        logger.info("Deleting loan offer", id=pk)
        await self.repository.delete(pk)
        logger.info("Deleted loan offer", id=pk)

    async def update(
            self,
            pk: ObjectId,
            data_object: fields.LoanOfferUpdate,
    ) -> fields.LoanOfferOut:
        """Update a loan_offer.
        Args:
            pk (ObjectId): loan_offer ID.
            data_object (LoanOfferUpdate): input data.
        Returns:
            LoanOfferOut: updated loan offer.
        """
        logger.info("Updating loan offer", id=pk, data=data_object)
        loan_offer = await self.repository.update(pk, data_object)
        logger.info("Updated loan offer", entry=borrower)
        return loan_offer

    async def update_many(
            self,
            ids: list[ObjectId],
            data_object: fields.LoanOfferUpdate,
    ) -> list[fields.LoanOfferOut]:
        """Update many loan offer.
        Args:
            ids (list[ObjectId]): list of loan offer IDs.
            data_object (LoanOfferUpdate): input data.
        Returns:
            list[LoanOfferOut]: list of updated loan offer.
        """
        logger.info("Updating loan offers", ids=ids, data=data_object)
        loan_offers = await self.repository.update_many(ids, data_object)
        logger.info("Updated loan offers", qty=len(loan_offers))
        return loan_offers
