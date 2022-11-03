"""Repositories for the loan informations domain."""

from lms.api.v1 import fields
from lms.database import models
from lms.domain.repositories import database


class LoanInformationsOdmRepository(
    database.MongoRepository[
        models.LoanInformation,
        fields.LoanInformationCreate,
        fields.LoanInformationUpdate,
        fields.LoanInformationOut,
    ],
):
    """Loan informations ODM repository."""

    table = models.LoanInformation
    schema = fields.LoanInformationOut
