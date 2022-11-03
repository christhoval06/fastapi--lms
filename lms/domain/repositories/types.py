"""Domain types."""

from typing import TypeVar

from lms.api import fields

CreateSchema = TypeVar(
    "CreateSchema",
    bound=fields.Interface,
    contravariant=True,
)

UpdateSchema = TypeVar(
    "UpdateSchema",
    bound=fields.InterfaceId,
    contravariant=True,
)

OutSchema = TypeVar("OutSchema", bound=fields.Interface)
