"""Model logic for the payments domain."""

import uuid

from structlog import get_logger
from bson import ObjectId

from lms.api.v1 import fields
from lms.domain.repositories import generic

logger = get_logger(__name__)


class PaymentService:
    """Orchestrator for the payments domain.
    Contains the business logic around the payments model operations.
    """

    def __init__(self, repository: generic.Repository) -> None:
        self.repository = repository

    async def create(
            self,
            data_object: fields.PaymentCreate,
    ) -> fields.PaymentOut:
        """Create a new payment.
        Args:
            data_object (PaymentCreate): input data.
        Returns:
            PaymentOut: representation of the created payment.
        """
        logger.info("Creating payment", data=data_object)
        logger.info("Creating payment", data=data_object)
        payment = await self.repository.create(data_object)
        logger.info("Created payment", entry=payment)
        return payment

    async def get_by_id(self, pk: ObjectId) -> fields.PaymentOut:
        """Get a payment by its ID.
        Args:
            pk (ObjectId): payment ID.
        Returns:
            PaymentOut: representation of the payment.
        """
        logger.info("Getting payment", id=pk)
        payment = await self.repository.get_by_id(pk)
        logger.info("Got payment by ID", entry=payment)
        return payment

    async def collect(self, **kwargs) -> list[fields.PaymentOut]:
        """Collect all payments.
        Returns:
            list[PaymentOut]: list of payments.
        """
        logger.info("Collecting payments")
        payments = await self.repository.collect(**kwargs)
        logger.info("Collected payments", qty=len(payments))
        return payments

    async def delete(self, pk: ObjectId) -> None:
        """Delete a payment.
        Args:
            pk (ObjectId): payment ID.
        """
        logger.info("Deleting payment", id=pk)
        await self.repository.delete(pk)
        logger.info("Deleted payment", id=pk)

    async def update(
            self,
            pk: ObjectId,
            data_object: fields.PaymentUpdate,
    ) -> fields.PaymentOut:
        """Update a payment.
        Args:
            pk (ObjectId): payment ID.
            data_object (PaymentUpdate): input data.
        Returns:
            PaymentOut: updated payment.
        """
        logger.info("Updating payment", id=pk, data=data_object)
        payment = await self.repository.update(pk, data_object)
        logger.info("Updated payment", entry=payment)
        return payment

    async def update_many(
            self,
            ids: list[ObjectId],
            data_object: fields.PaymentUpdate,
    ) -> list[fields.PaymentOut]:
        """Update many payments.
        Args:
            ids (list[ObjectId]): list of payment IDs.
            data_object (PaymentUpdate): input data.
        Returns:
            list[PaymentOut]: list of updated payments.
        """
        logger.info("Updating payments", ids=ids, data=data_object)
        payments = await self.repository.update_many(ids, data_object)
        logger.info("Updated payments", qty=len(payments))
        return payments
