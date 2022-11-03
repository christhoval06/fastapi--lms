"""Set of pre-instantiated dependencies for the borrowers domain."""

from lms.domain.generic.registry import GenericRegistry

from .repository import BorrowersOdmRepository
from .service import BorrowerService

borrowers_registry = GenericRegistry(repository=BorrowersOdmRepository(), service=BorrowerService)
