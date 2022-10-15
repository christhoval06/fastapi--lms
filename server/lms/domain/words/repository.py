"""Repositories for the words domain."""

from panama.api.v1 import fields
from panama.database import models
from panama.domain.repositories import database


class WordsOdmRepository(
    database.MongoRepository[
        models.Word,
        fields.WordCreate,
        fields.WordUpdate,
        fields.WordOut,
    ],
):
    """Words ODM repository."""

    table = models.Word
    schema = fields.WordOut
