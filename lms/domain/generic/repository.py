"""Repositories for the borrowers domain."""

from lms.api.v1 import fields
from lms.database import models
from lms.domain.repositories import database, generic


class GenericOdmRepository(
    database.MongoRepository[
        models.Borrower,
        fields.BorrowerCreate,
        fields.BorrowerUpdate,
        fields.BorrowerOut,
    ]
):
    """Borrowers ODM repository."""

    def __init__(self, table, schema):
        self.table = table
        self.schema = schema
