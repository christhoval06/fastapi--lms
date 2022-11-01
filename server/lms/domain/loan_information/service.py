"""Model logic for the loan informations domain."""

import uuid

from structlog import get_logger

from lms.api.v1 import fields
from lms.domain.repositories import generic

logger = get_logger(__name__)


class LoanInformationService:
    """Orchestrator for the loan informations domain.
    Contains the business logic around the loan informations model operations.
    """

    def __init__(self, repository: generic.Repository) -> None:
        self.repository = repository

    async def create(
            self,
            data_object: fields.LoanInformationCreate,
    ) -> fields.LoanInformationOut:
        """Create a new loan_information.
        Args:
            data_object (LoanInformationCreate): input data.
        Returns:
            LoanInformationOut: representation of the created loan_information.
        """
        logger.info("Creating loan informations", data=data_object)
        logger.info("Creating loan informations", data=data_object)
        loan_information = await self.repository.create(data_object)
        logger.info("Created loan informations", entry=loan_information)
        return loan_information

    async def get_by_id(self, pk: uuid.UUID) -> fields.LoanInformationOut:
        """Get a loan_information by its ID.
        Args:
            pk (UUID): loan_information ID.
        Returns:
            LoanInformationOut: representation of the loan_information.
        """
        logger.info("Getting loan informations", id=pk)
        loan_information = await self.repository.get_by_id(pk)
        logger.info("Got loan informations by ID", entry=loan_information)
        return loan_information

    async def collect(self, **kwargs) -> list[fields.LoanInformationOut]:
        """Collect all loan informations.
        Returns:
            list[LoanInformationOut]: list of loan informations.
        """
        logger.info("Collecting loan informations")
        loan_informations = await self.repository.collect(**kwargs)
        logger.info("Collected loan informations", qty=len(loan_informations))
        return loan_informations

    async def delete(self, pk: uuid.UUID) -> None:
        """Delete a loan_information.
        Args:
            pk (UUID): loan_information ID.
        """
        logger.info("Deleting loan_information", id=pk)
        await self.repository.delete(pk)
        logger.info("Deleted loan_information", id=pk)

    async def update(
            self,
            pk: uuid.UUID,
            data_object: fields.LoanInformationUpdate,
    ) -> fields.LoanInformationOut:
        """Update a loan_information.
        Args:
            pk (UUID): loan_information ID.
            data_object (LoanInformationUpdate): input data.
        Returns:
            LoanInformationOut: updated loan_information.
        """
        logger.info("Updating loan informations", id=pk, data=data_object)
        loan_information = await self.repository.update(pk, data_object)
        logger.info("Updated loan informations", entry=loan_information)
        return loan_information

    async def update_many(
            self,
            ids: list[uuid.UUID],
            data_object: fields.LoanInformationUpdate,
    ) -> list[fields.LoanInformationOut]:
        """Update many loan_informations.
        Args:
            ids (list[UUID]): list of loan_information IDs.
            data_object (LoanInformationUpdate): input data.
        Returns:
            list[LoanInformationOut]: list of updated loan informations.
        """
        logger.info("Updating loan informations", ids=ids, data=data_object)
        loan_informations = await self.repository.update_many(ids, data_object)
        logger.info("Updated loan informations", qty=len(loan_informations))
        return loan_informations
