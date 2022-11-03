"""Set of pre-instantiated dependencies for the reports domain."""

from lms.domain.generic.registry import GenericRegistry

from lms.domain.reports.repository import ReportsOdmRepository
from lms.domain.reports.service import ReportService

reports_registry = GenericRegistry(repository=ReportsOdmRepository(), service=ReportService)
