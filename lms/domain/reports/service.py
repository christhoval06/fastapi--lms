"""Model logic for the reports domain."""

import uuid

from structlog import get_logger
from bson import ObjectId

from lms.api.v1 import fields
from lms.domain.repositories import generic

logger = get_logger(__name__)


class ReportService:
    """Orchestrator for the reports domain.
    Contains the business logic around the reports model operations.
    """

    def __init__(self, repository: generic.Repository) -> None:
        self.repository = repository

    async def create(
            self,
            data_object: fields.ReportCreate,
    ) -> fields.ReportOut:
        """Create a new report.
        Args:
            data_object (ReportCreate): input data.
        Returns:
            ReportOut: representation of the created report.
        """
        logger.info("Creating report", data=data_object)
        logger.info("Creating report", data=data_object)
        report = await self.repository.create(data_object)
        logger.info("Created report", entry=report)
        return report

    async def get_by_id(self, pk: ObjectId) -> fields.ReportOut:
        """Get a report by its ID.
        Args:
            pk (ObjectId): report ID.
        Returns:
            ReportOut: representation of the report.
        """
        logger.info("Getting report", id=pk)
        report = await self.repository.get_by_id(pk)
        logger.info("Got report by ID", entry=report)
        return report

    async def collect(self) -> list[fields.ReportOut]:
        """Collect all reports.
        Returns:
            list[ReportOut]: list of reports.
        """
        logger.info("Collecting reports")
        reports = await self.repository.collect()
        logger.info("Collected reports", qty=len(reports))
        return reports

    async def delete(self, pk: ObjectId) -> None:
        """Delete a report.
        Args:
            pk (ObjectId): report ID.
        """
        logger.info("Deleting report", id=pk)
        await self.repository.delete(pk)
        logger.info("Deleted report", id=pk)

    async def update(
            self,
            pk: ObjectId,
            data_object: fields.ReportUpdate,
    ) -> fields.ReportOut:
        """Update a report.
        Args:
            pk (ObjectId): report ID.
            data_object (ReportUpdate): input data.
        Returns:
            ReportOut: updated report.
        """
        logger.info("Updating report", id=pk, data=data_object)
        report = await self.repository.update(pk, data_object)
        logger.info("Updated report", entry=report)
        return report

    async def update_many(
            self,
            ids: list[ObjectId],
            data_object: fields.ReportUpdate,
    ) -> list[fields.ReportOut]:
        """Update many reports.
        Args:
            ids (list[ObjectId]): list of report IDs.
            data_object (ReportUpdate): input data.
        Returns:
            list[ReportOut]: list of updated reports.
        """
        logger.info("Updating reports", ids=ids, data=data_object)
        reports = await self.repository.update_many(ids, data_object)
        logger.info("Updated reports", qty=len(reports))
        return reports
