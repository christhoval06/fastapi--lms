"""Repository-level exceptions."""

from bson import ObjectId
from dataclasses import dataclass


@dataclass
class DoesNotExistError(Exception):
    """Raised when an object does not exist."""

    id: ObjectId
