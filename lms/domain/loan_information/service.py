"""Model logic for the loan information domain."""

from structlog import get_logger

from lms.api.v1 import fields
from lms.domain.generic.service import GenericService

logger = get_logger(__name__)


class LoanInformationService(GenericService[fields.LoanInformationOut, fields.LoanInformationCreate, fields.LoanInformationUpdate]):
    pass
