"""Database models."""

import datetime
from enum import Enum
from decimal import Decimal

import pymongo
from bson import objectid, ObjectId

import strawberry
from beanie import Document, Indexed, Link, PydanticObjectId
from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class Model(Document):
    """Document model abstraction."""

    id: PydanticObjectId = Field(default_factory=objectid.ObjectId, alias='_id')
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)


@strawberry.type
class Admin(Model):
    fullname: str
    email: EmailStr
    password: str
    active: bool

    class Collection:
        name = "admins"

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Christhoval Barba",
                "email": "me@christhoval.dev",
                "password": "$ecr3tP@ss"
            }
        }


@strawberry.enum
class Gender(Enum):
    MALE = 0
    FEMALE = 1


class Borrower(Model):
    """Borrower document model."""

    name: str
    phone_number: str
    age: int
    address: str
    gender: Gender

    class Settings:
        name = "borrowers"
        indexes = [
            [
                ("name", pymongo.TEXT),
            ],
        ]


@strawberry.enum
class PaymentRange(Enum):
    DAILY = 0
    WEEKLY = 1
    BIWEEKLY = 2
    MONTHLY = 3
    BIMONTHLY = 4
    QUARTERLY = 5
    SEMIANNUALLY = 6
    ANNUALLY = 7


class LoanInformation(Model):
    """LoanInformation document model."""

    borrower_id: PydanticObjectId
    loan_date: datetime.datetime = Field(default_factory=datetime.datetime.now)
    loan_due: Decimal
    payment_range: PaymentRange

    class Settings:
        name = "loans_information"


class LoanOffer(Model):
    loan_name: str
    amount: Decimal
    loan_range: PaymentRange
    interest: float

    class Settings:
        name = "loan_offers"


class Payment(Model):
    information_id: PydanticObjectId
    borrower_id: PydanticObjectId
    amount: Decimal
    interest: Decimal
    total: Decimal
    paymment_date: datetime.datetime = Field(default_factory=datetime.datetime.now)

    class Settings:
        name = "payments"


class Report(Model):
    borrower_id: PydanticObjectId
    payment_id: PydanticObjectId
    information_id: PydanticObjectId
    loan_id: PydanticObjectId
    date: datetime.datetime = Field(default_factory=datetime.datetime.now)

    class Settings:
        name = "reports"
