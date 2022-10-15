"""GraphQL resolver functions."""

import uuid


from bson import ObjectId
from strawberry.types import Info

from lms.api.v1 import fields
from lms.api import fields as base_fields
from lms.domain import borrowers_srv, linfo_srv

from lms.database import models


async def get_borrower(borrower_id: base_fields.PyObjectId) -> fields.BorrowerOut:
    """Fetch a Borrower.
    Returns:
        Borrower: retrieved borrower.
    """
    return await borrowers_srv.get_by_id(borrower_id)


async def get_borrowers() -> list[fields.BorrowerOut]:
    """Fetch all the Borrower.
    Returns:
        list[Borrower]: retrieved borrower.
    """
    return await borrowers_srv.collect()


async def create_borrower(data: fields.BorrowerCreate, info: Info) -> fields.BorrowerOut:
    """Create new borrower.
    Args:
        # data_object (BorrowerCreate): input data.
    Returns:
        Borrower: updated Borrower.
    """
    return await borrowers_srv.create(data)


async def get_loans_information() -> list[fields.LoanInformationOut]:
    """Fetch all the LoanInformation.
    Returns:
        list[LoanInformation]: retrieved loan information.
    """
    return await linfo_srv.collect()


async def create_loan_information(data: fields.LoanInformationCreate) -> fields.LoanInformationOut:
    """Create new LoanInformation.
    Args:
        # data_object (LoanInformationCreate): input data.
    Returns:
        Borrower: updated LoanInformation.
    """
    return await linfo_srv.create(data)
