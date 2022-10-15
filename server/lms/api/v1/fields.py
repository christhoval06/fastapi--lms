"""GraphQL API fields."""

import datetime
import uuid
from typing import Union, Optional, NewType
from pydantic import BaseModel

import strawberry
from strawberry.types import Info

from bson import ObjectId
from beanie import PydanticObjectId

from lms.api import fields
# from lms.domain import borrowers_srv, linfo_srv
from lms.database import models


@strawberry.experimental.pydantic.input(model=models.Borrower, fields=["name", "phone_number", "age", "address", "gender"])
class BorrowerCreate(fields.Interface):
    """Borrower input API model."""
    pass


@strawberry.experimental.pydantic.type(model=models.Borrower,
                                       fields=['created_at', 'name', 'phone_number', 'age', 'address', 'gender'])
class BorrowerOut(fields.Interface):
    """Borrower output API model."""

    id: fields.PyObjectId

    @strawberry.field
    def created_at_formatted(self, formatted: Optional[str] = '%d/%m/%Y') -> str:
        return self.created_at.strftime(formatted)


@strawberry.type
class BorrowerUpdate(fields.InterfaceId):
    """Borrower update input API model."""

    name: Union[str, None] = None
    phone_number: Union[str, None] = None
    age: Union[int, None] = None
    address: Union[str, None] = None
    gender: Union[str, None] = None


@strawberry.experimental.pydantic.input(model=models.LoanInformation, fields=['created_at', 'loan_date', 'loan_due', 'payment_range'])
class LoanInformationCreate(fields.Interface):
    """LoanInformation input API model."""
    borrower_id: fields.PyObjectId


@strawberry.experimental.pydantic.type(model=models.LoanInformation, fields=['created_at', 'loan_date', 'loan_due', 'payment_range'])
class LoanInformationOut(fields.Interface):
    """LoanInformation output API model."""

    id: fields.PyObjectId
    created_at: datetime.datetime

    borrower_id: fields.PyObjectId
    loan_date: datetime.datetime
    loan_due: float
    payment_range: models.PaymentRange

    @strawberry.field
    async def borrower(self, info: Info) -> BorrowerOut:
        return await info.context.borrowers_srv.get_by_id(self.borrower_id)

    @strawberry.field
    def created_at_formatted(self, formatted: Optional[str] = '%d/%m/%Y') -> str:
        return self.created_at.strftime(formatted)

    @strawberry.field
    def loan_date_formatted(self, formatted: Optional[str] = '%d/%m/%Y') -> str:
        return self.loan_date.strftime(formatted)


@strawberry.type
class LoanInformationUpdate(fields.InterfaceId):
    """LoanInformation update input API model."""

    name: Union[str, None] = None
    phone_number: Union[str, None] = None
    age: Union[int, None] = None
    address: Union[str, None] = None
    gender: Union[str, None] = None
