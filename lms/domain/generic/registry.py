"""Set of pre-instantiated dependencies for the generic domain."""
from lms.domain.generic.service import GenericService


class GenericRegistry:
    """Registry of dependencies for the generic domain."""

    def __init__(self, repository, service=GenericService):
        self.service = service(repository=repository)
