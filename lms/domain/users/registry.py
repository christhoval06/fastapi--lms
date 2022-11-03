"""Set of pre-instantiated dependencies for the users domain."""
from lms.domain.generic.registry import GenericRegistry

from .repository import UsersOdmRepository
from .service import UsersService

users_registry = GenericRegistry(repository=UsersOdmRepository(), service=UsersService)
