"""Set of pre-instantiated dependencies for the reports domain."""

from lms.domain.reports.repository import ReportsOdmRepository
from lms.domain.reports.service import ReportService


class ReportsRegistry:
    """Registry of dependencies for the reports domain."""

    service = ReportService(repository=ReportsOdmRepository())


reports_registry = ReportsRegistry()
