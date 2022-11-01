"""Repositories for the reports domain."""

from lms.api.v1 import fields
from lms.database import models
from lms.domain.repositories import database, generic


class ReportsOdmRepository(
    database.MongoRepository[
        models.Report,
        fields.ReportCreate,
        fields.ReportUpdate,
        fields.ReportOut,
    ]
):
    """Reports ODM repository."""

    table = models.Report
    schema = fields.ReportOut
