"""Model logic for the payments domain."""

from bson import ObjectId
from structlog import get_logger

from lms.api.v1 import fields
from lms.domain.generic.service import GenericService

logger = get_logger(__name__)


class PaymentService(GenericService[fields.PaymentOut, fields.PaymentCreate, fields.PaymentUpdate]):
    pass
