"""Set of pre-instantiated dependencies for the loan informations domain."""

from lms.domain.generic.registry import GenericRegistry

from .repository import LoanInformationsOdmRepository
from .service import LoanInformationService

loans_information_registry = GenericRegistry(repository=LoanInformationsOdmRepository(), service=LoanInformationService)
