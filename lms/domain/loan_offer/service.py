"""Model logic for the loan offer domain."""

from structlog import get_logger

from lms.api.v1 import fields
from lms.domain.generic.service import GenericService

logger = get_logger(__name__)


class LoanOfferService(GenericService[fields.LoanOfferOut, fields.LoanOfferCreate, fields.LoanOfferUpdate]):
    pass
