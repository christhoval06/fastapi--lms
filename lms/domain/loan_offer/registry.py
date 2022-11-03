"""Set of pre-instantiated dependencies for the loan offer domain."""

from lms.domain.generic.registry import GenericRegistry

from .repository import LoanOfferOdmRepository
from .service import LoanOfferService

loan_offer_registry = GenericRegistry(repository=LoanOfferOdmRepository(), service=LoanOfferService)
