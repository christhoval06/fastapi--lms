"""Repositories for the borrowers domain."""

from lms.api.v1 import fields
from lms.database import models
from lms.domain.repositories import database, generic


class UsersOdmRepository(
    database.MongoRepository[
        models.Admin,
        fields.AdminCreate,
        fields.AdminUpdate,
        fields.AdminOut,
    ]
):
    """Borrowers ODM repository."""

    def __init__(self):
        self.table = models.Admin
        self.schema = fields.AdminOut
