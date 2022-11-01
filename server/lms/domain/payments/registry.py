"""Set of pre-instantiated dependencies for the payments domain."""

from lms.domain.payments.repository import PaymentsOdmRepository
from lms.domain.payments.service import PaymentService


class PaymentsRegistry:
    """Registry of dependencies for the payments domain."""

    service = PaymentService(repository=PaymentsOdmRepository())


payments_registry = PaymentsRegistry()
