"""Repositories for the borrowers domain."""

from lms.api.v1 import fields
from lms.database import models
from lms.domain.repositories import database, generic


class BorrowersOdmRepository(
    database.MongoRepository[
        models.Borrower,
        fields.BorrowerCreate,
        fields.BorrowerUpdate,
        fields.BorrowerOut,
    ]
):
    """Borrowers ODM repository."""

    table = models.Borrower
    schema = fields.BorrowerOut
