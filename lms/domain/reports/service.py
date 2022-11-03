"""Model logic for the reports domain."""

from structlog import get_logger

from lms.api.v1 import fields
from lms.domain.generic.service import GenericService

logger = get_logger(__name__)


class ReportService(GenericService[fields.ReportOut, fields.ReportCreate, fields.ReportUpdate]):
    pass
