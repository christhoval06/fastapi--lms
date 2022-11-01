"""Set of pre-instantiated dependencies for the loan offer domain."""

from lms.domain.loan_offer.repository import LoanOfferOdmRepository
from lms.domain.loan_offer.service import LoanOfferService


class LoanOfferRegistry:
    """Registry of dependencies for the loan offer domain."""

    service = LoanOfferService(repository=LoanOfferOdmRepository())


loan_offer_registry = LoanOfferRegistry()
