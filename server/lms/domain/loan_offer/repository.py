"""Repositories for the loan offer domain."""

from lms.api.v1 import fields
from lms.database import models
from lms.domain.repositories import database, generic


class LoanOfferOdmRepository(
    database.MongoRepository[
        models.LoanOffer,
        fields.LoanOfferCreate,
        fields.LoanOfferUpdate,
        fields.LoanOfferOut,
    ]
):
    """LoanOffer ODM repository."""

    table = models.LoanOffer
    schema = fields.LoanOfferOut
