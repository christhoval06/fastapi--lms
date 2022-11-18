"""GraphQL API fields."""

import datetime
from decimal import Decimal
from typing import Union, Optional, NewType, List, Generic, TypeVar

import strawberry
from beanie import PydanticObjectId
from bson import ObjectId
from pydantic import BaseModel, EmailStr
from strawberry.types import Info

from lms.api import fields
from lms.database import models

T = TypeVar("T")


@strawberry.type
class ModelOutPaginate(Generic[T]):
    total: int
    limit: int
    page: int
    has_next: bool
    data: list[T]


@strawberry.experimental.pydantic.input(model=models.Borrower,
                                        fields=["name", "phone_number", "age", "address", "gender"])
class BorrowerCreate(fields.Interface):
    """Borrower input API model."""
    pass


@strawberry.experimental.pydantic.type(model=models.Borrower,
                                       fields=['created_at', 'name', 'phone_number', 'age', 'address', 'gender'])
class BorrowerOut(fields.Interface):
    """Borrower output API model."""

    id: fields.PyObjectId


@strawberry.type
class BorrowerUpdate(fields.InterfaceId):
    """Borrower update input API model."""

    name: Union[str, None] = None
    phone_number: Union[str, None] = None
    age: Union[int, None] = None
    address: Union[str, None] = None
    gender: Union[str, None] = None


@strawberry.experimental.pydantic.input(model=models.LoanInformation,
                                        fields=['created_at', 'loan_date', 'payment_range'])
class LoanInformationCreate(fields.Interface):
    """LoanInformation input API model."""
    borrower_id: fields.PyObjectId
    loan_due: Decimal


@strawberry.experimental.pydantic.type(model=models.LoanInformation,
                                       fields=['created_at', 'loan_date', 'payment_range'])
class LoanInformationOut(fields.Interface):
    """LoanInformation output API model."""

    id: fields.PyObjectId
    created_at: datetime.datetime

    borrower_id: fields.PyObjectId
    loan_date: datetime.datetime
    loan_due: Decimal
    payment_range: models.PaymentRange

    @strawberry.field
    async def borrower(self, info: Info) -> BorrowerOut:
        return await info.context.borrowers_srv.get_by_id(self.borrower_id)

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


@strawberry.experimental.pydantic.input(model=models.LoanOffer,
                                        fields=['created_at', 'loan_name', 'amount', 'loan_range', 'interest'])
class LoanOfferCreate(fields.Interface):
    """LoanOffer input API model."""
    pass


@strawberry.experimental.pydantic.type(model=models.LoanOffer,
                                       fields=['created_at', 'loan_name', 'amount', 'loan_range', 'interest'])
class LoanOfferOut(fields.Interface):
    """LoanOffer output API model."""

    id: fields.PyObjectId


@strawberry.type
class LoanOfferUpdate(fields.InterfaceId):
    """LoanOffer update input API model."""

    loan_name: Union[str, None] = None
    amount: Union[Decimal, None] = None
    loan_range: Union[models.PaymentRange, None] = None
    interest: Union[float, None] = None


@strawberry.experimental.pydantic.input(model=models.Payment,
                                        fields=['created_at', 'interest', 'amount', 'total', 'paymment_date'])
class PaymentCreate(fields.Interface):
    """Payment input API model."""
    information_id: fields.PyObjectId
    borrower_id: fields.PyObjectId


@strawberry.experimental.pydantic.type(model=models.Payment,
                                       fields=['created_at', 'interest', 'amount', 'total', 'paymment_date'])
class PaymentOut(fields.Interface):
    """Payment output API model."""

    id: fields.PyObjectId
    information_id: fields.PyObjectId
    borrower_id: fields.PyObjectId

    @strawberry.field
    async def borrower(self, info: Info) -> BorrowerOut:
        return await info.context.borrowers_srv.get_by_id(self.borrower_id)

    @strawberry.field
    async def information(self, info: Info) -> LoanInformationOut:
        return await info.context.linfo_srv.get_by_id(self.information_id)


@strawberry.type
class PaymentUpdate(fields.InterfaceId):
    """Payment update input API model."""

    information_id: Optional[fields.PyObjectId] = None
    borrower_id: Optional[fields.PyObjectId] = None

    amount: Union[Decimal, None] = None
    interest: Union[Decimal, None] = None
    total: Union[Decimal, None] = None
    loan_range: Union[models.PaymentRange, None] = None
    paymment_date: Union[datetime.datetime, None] = None


@strawberry.experimental.pydantic.input(model=models.Report, fields=['created_at', 'date'])
class ReportCreate(fields.Interface):
    """Report input API model."""
    information_id: fields.PyObjectId
    borrower_id: fields.PyObjectId


@strawberry.experimental.pydantic.type(model=models.Report, fields=['created_at', 'date'])
class ReportOut(fields.Interface):
    """Report output API model."""

    id: fields.PyObjectId
    borrower_id: fields.PyObjectId
    information_id: fields.PyObjectId
    payment_id: fields.PyObjectId
    loan_id: fields.PyObjectId

    @strawberry.field
    async def borrower(self, info: Info) -> BorrowerOut:
        return await info.context.borrowers_srv.get_by_id(self.borrower_id)

    @strawberry.field
    async def information(self, info: Info) -> LoanInformationOut:
        return await info.context.linfo_srv.get_by_id(self.information_id)

    @strawberry.field
    async def payment(self, info: Info) -> PaymentOut:
        return await info.context.payments_srv.get_by_id(self.payment_id)

    @strawberry.field
    async def loan(self, info: Info) -> LoanOfferOut:
        return await info.context.loan_offer_srv.get_by_id(self.loan_id)


@strawberry.type
class ReportUpdate(fields.InterfaceId):
    """Payment update input API model."""

    borrower_id: Optional[fields.PyObjectId] = None
    payment_id: Optional[fields.PyObjectId] = None
    information_id: Optional[fields.PyObjectId] = None
    loan_id: Optional[fields.PyObjectId] = None

    date: Union[datetime.datetime, None] = None


@strawberry.experimental.pydantic.input(model=models.Admin,
                                        fields=['full_name', 'password', 'email', 'active'])
class AdminCreate(fields.Interface):
    """Admin input API model."""
    pass


@strawberry.experimental.pydantic.type(model=models.Admin, fields=['created_at', 'full_name', 'email', 'active'])
class AdminOut(fields.Interface):
    """Admin output API model."""

    id: fields.PyObjectId

    # information_id: fields.PyObjectId
    # borrower_id: fields.PyObjectId

    # @strawberry.field
    # async def borrower(self, info: Info) -> BorrowerOut:
    #     return await info.context.borrowers_srv.get_by_id(self.borrower_id)
    #
    # @strawberry.field
    # async def information(self, info: Info) -> LoanInformationOut:
    #     return await info.context.linfo_srv.get_by_id(self.information_id)


@strawberry.type
class AdminUpdate(fields.InterfaceId):
    """Admin update input API model."""

    full_name: Union[str, None] = None
    email: Union[EmailStr, None] = None
    active: Union[bool, None] = None


@strawberry.input
class AuthLoginInput:
    username: str
    password: str


@strawberry.type
class AuthToken:
    access_token: str
    refresh_token: str
    full_name: str
    email: str
