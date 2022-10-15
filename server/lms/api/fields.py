"""API interfaces."""

import typing as T
import uuid

import strawberry
from beanie import Document, PydanticObjectId
from bson import objectid, ObjectId

M = T.TypeVar("M", bound="Interface")

PyObjectId = strawberry.scalar(
    T.NewType("PyObjectId", T.Union[str, ObjectId]),
    serialize=lambda v: str(v),
    parse_value=lambda v: ObjectId(v),
)


class Interface:
    """Generic API interface."""

    @classmethod
    def from_orm(cls: type[M], entry: Document) -> M:
        """Create a new instance from an ORM entry.
        Args:
            entry (Document): ORM entry.
        Returns:
            InterfaceObj: new instance.
        """
        return cls(**entry.dict())

    def to_dict(self, exclude_unset=False) -> dict:
        """Convert the instance to a dict.
        Args:
            exclude_unset (bool): whether to exclude unset fields.
        Returns:
            dict: dict representation.
        """
        if not exclude_unset:
            return self.__dict__

        return {
            key: value
            for key, value in self.__dict__.items()
            if value is not None
        }


@strawberry.interface
class InterfaceId(Interface):
    """Generic API interface."""

    def __init__(self, **kwargs) -> None:
        """Allow taking parameters.
        Note:
            Mypy seems to be confused about missing init.
        Args:
            kwargs: additional keyword arguments.
        """

    @strawberry.field
    def _id(self) -> PyObjectId:
        """Generate a random ObjectId.
        Simple object identifier, just to satisfy the interface API.
        Returns:
            PyObjectId: random ObjectId.
        """

        if 'id' in self.__dict__:
            return self.id
        return PyObjectId(objectid.ObjectId())
