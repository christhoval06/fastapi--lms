"""Set of pre-instantiated dependencies for the loan informations domain."""

from lms.domain.loan_information.repository import LoanInformationsOdmRepository
from lms.domain.loan_information.service import LoanInformationService


class LoanInformationsRegistry:
    """Registry of dependencies for the loan informations domain."""

    service = LoanInformationService(repository=LoanInformationsOdmRepository())


loan_informations_registry = LoanInformationsRegistry()
