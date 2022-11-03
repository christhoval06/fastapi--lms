"""Model logic for the borrowers domain."""

from structlog import get_logger

from lms.api.v1 import fields
from lms.domain.generic.service import GenericService

logger = get_logger(__name__)


class BorrowerService(GenericService[fields.BorrowerOut, fields.BorrowerCreate, fields.BorrowerUpdate]):
    pass
