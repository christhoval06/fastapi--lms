"""Repository-level exceptions."""

from dataclasses import dataclass

from bson import ObjectId


@dataclass
class DoesNotExistError(Exception):
    """Raised when an object does not exist."""

    id: ObjectId
    message: str = None


@dataclass
class DoesExistError(Exception):
    """Raised when an object does exist."""

    message: str = None
