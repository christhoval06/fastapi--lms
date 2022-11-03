"""Set of pre-instantiated dependencies for the generic domain."""

from lms.domain.generic.repository import GenericOdmRepository
from lms.domain.generic.service import GenericService


class GenericRegistry:
    """Registry of dependencies for the generic domain."""

    def __init__(self, table, schema):
        self.service = GenericService(repository=GenericOdmRepository(table, schema))
