"""Repository abstractions."""

import typing as T
from bson import ObjectId
from beanie import Document

from lms.domain.repositories import types

M = T.TypeVar("M", bound=Document)


class Repository(
    T.Generic[
        M,
        types.CreateSchema,
        types.UpdateSchema,
        types.OutSchema,
    ],
    T.Protocol,
):
    """Abstraction over the idea of persistent storage.
    Interface class for all the concrete repository implementations.
    """
    table: type[M]
    schema: type[types.OutSchema]

    async def create(self, data_object: types.CreateSchema, **kwargs) -> types.OutSchema:
        """Create a new entry.
        Args:
            data_object (types.CreateSchema): input data object.
        """
        ...  # noqa: WPS428

    async def get_by_id(self, entry_id: ObjectId) -> types.OutSchema:
        """Get an entry by its identifier.
        Args:
            entry_id (ObjectId): entry ID.
        """
        ...  # noqa: WPS428

    async def collect(
            self,
            **filters,
    ) -> list[types.OutSchema]:
        """Collect all entries and allow filtering.
        Args:
            filters (dict): additional filters to apply.
        """
        ...  # noqa: WPS428

    async def delete(self, entry_id: ObjectId) -> None:
        """Delete an entry.
        Args:
            entry_id (ObjectId): entry ID.
        """
        ...  # noqa: WPS428

    async def update(
            self,
            entry_id: ObjectId,
            data_object: types.UpdateSchema,
    ) -> types.OutSchema:
        """Update an existing entry.
        Args:
            entry_id (ObjectId): entry ID.
            data_object (types.UpdateSchema): input data object.
        """
        ...  # noqa: WPS428

    async def update_many(
            self,
            entry_ids: list[ObjectId],
            data_object: types.UpdateSchema,
    ) -> list[types.OutSchema]:
        """Update multiple entries.
        Args:
            entry_ids (list[ObjectId]): list of entry IDs.
            data_object (types.UpdateSchema): input data object.
        """
        ...  # noqa: WPS428
