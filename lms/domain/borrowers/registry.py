"""Set of pre-instantiated dependencies for the borrowers domain."""

from lms.domain.borrowers.repository import BorrowersOdmRepository
from lms.domain.borrowers.service import BorrowerService


class BorrowersRegistry:
    """Registry of dependencies for the borrowers domain."""

    service = BorrowerService(repository=BorrowersOdmRepository())


borrowers_registry = BorrowersRegistry()
