"""GraphQL resolver functions."""

import uuid

from bson import ObjectId
from strawberry.types import Info
from typing import Optional

from lms.api import fields as base_fields
from lms.api.v1 import fields
from lms.database import models
from lms.domain import borrowers_srv, linfo_srv, loan_offer_srv, payments_srv, reports_srv, users_srv


async def get_borrowers(page: Optional[int] = 0, limit: Optional[int] = 12) -> fields.ModelOutPaginate[fields.BorrowerOut]:
    """Fetch all the Borrower.
    Returns:
        list[Borrower]: retrieved borrower.
    """
    return await borrowers_srv.paginate(page, limit)


async def get_borrower(borrower_id: base_fields.PyObjectId) -> fields.BorrowerOut:
    """Fetch a Borrower.
    Returns:
        Borrower: retrieved borrower.
    """
    return await borrowers_srv.get_by_id(borrower_id)


async def get_borrower_loans(borrower_id: base_fields.PyObjectId, info: Info) -> list[fields.LoanInformationOut]:
    """Fetch all the Borrower Loans.
    Returns:
        list[LoanInformationOut]: retrieved borrower.
    """
    print("borrower_id", str(borrower_id))
    return await info.context.linfo_srv.collect(borrower_id=borrower_id)


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


async def get_loan_information(information_id: base_fields.PyObjectId) -> fields.LoanInformationOut:
    """Fetch a LoanInformation.
    Returns:
        LoanInformation: retrieved loan information.
    """
    return await linfo_srv.get_by_id(information_id)


async def create_loan_information(data: fields.LoanInformationCreate) -> fields.LoanInformationOut:
    """Create new LoanInformation.
    Args:
        # data_object (LoanInformationCreate): input data.
    Returns:
        Borrower: updated LoanInformation.
    """
    return await linfo_srv.create(data)


async def get_loan_information_payments(information_id: base_fields.PyObjectId, info: Info) -> list[fields.PaymentOut]:
    """Fetch all the PaymentOut for Loans.
    Returns:
        list[PaymentOut]: retrieved borrower.
    """
    return await info.context.payments_srv.collect(information_id=information_id)


async def get_loans_offers() -> list[fields.LoanOfferOut]:
    """Fetch all the LoanOffer.
    Returns:
        list[LoanOffer]: retrieved loan offer.
    """
    return await loan_offer_srv.collect()


async def get_loan_offer(loan_id: base_fields.PyObjectId) -> fields.LoanOfferOut:
    """Fetch all the LoanOffer.
    Returns:
        LoanOffer: retrieved loan offer.
    """
    return await loan_offer_srv.get_by_id(loan_id)


async def get_payments() -> list[fields.PaymentOut]:
    """Fetch all the PaymentOut.
    Returns:
        list[PaymentOut]: retrieved payments.
    """
    return await payments_srv.collect()


async def get_payment(payment_id: base_fields.PyObjectId) -> fields.PaymentOut:
    """Fetch all the PaymentOut.
    Returns:
        PaymentOut: retrieved reports.
    """
    return await payments_srv.get_by_id(payment_id)


async def get_reports() -> list[fields.ReportOut]:
    """Fetch all the ReportOut.
    Returns:
        list[ReportOut]: retrieved reports.
    """
    return await reports_srv.collect()


async def get_report(report_id: base_fields.PyObjectId) -> fields.ReportOut:
    """Fetch all the ReportOut.
    Returns:
        ReportOut: retrieved reports.
    """
    return await reports_srv.get_by_id(report_id)


async def create_user(data: fields.AdminCreate) -> fields.AdminOut:
    """Create new user.
        Args:
            # data_object (AdminCreate): input data.
        Returns:
            AdminOut: created Admin.
        """
    return await users_srv.create(data)


async def user_login(username: str, password: str) -> fields.LoginSuccess:
    """
    Sign In exists user.
    :param username: str
    :param password: str
    :return:
    """
    return await users_srv.login(username, password)
