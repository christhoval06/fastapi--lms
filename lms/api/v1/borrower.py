from fastapi import APIRouter, Body

from lms.domain.borrowers.registry import borrowers_registry
from lms.database.models import Borrower
from lms.api.v1 import fields

router = APIRouter()

borrowers_srv = borrowers_registry.service


@router.post("/", response_description="Add new Borrower", response_model=Borrower)
async def create_place(data: fields.BorrowerCreate = Body(...)) -> Borrower:
    borrower = await borrowers_srv.create(data)
    return borrower
