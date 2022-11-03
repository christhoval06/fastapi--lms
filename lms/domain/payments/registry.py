"""Set of pre-instantiated dependencies for the payments domain."""

from lms.domain.generic.registry import GenericRegistry

from lms.domain.payments.repository import PaymentsOdmRepository
from lms.domain.payments.service import PaymentService

payments_registry = GenericRegistry(repository=PaymentsOdmRepository(), service=PaymentService)
