"""Repositories for the payments domain."""

from lms.api.v1 import fields
from lms.database import models
from lms.domain.repositories import database, generic


class PaymentsOdmRepository(
    database.MongoRepository[
        models.Payment,
        fields.PaymentCreate,
        fields.PaymentUpdate,
        fields.PaymentOut,
    ]
):
    """Payments ODM repository."""

    table = models.Payment
    schema = fields.PaymentOut
