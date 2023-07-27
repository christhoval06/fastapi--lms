"""Set of pre-instantiated dependencies for the generic domain."""
from lms.domain import generic
from lms.domain.generic.service import GenericService
from lms.domain.repositories import generic


class GenericRegistry:
    """Registry of dependencies for the generic domain."""

    def __init__(self, repository: generic.Repository, service=GenericService):
        self.service = service(repository=repository)
