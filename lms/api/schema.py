import strawberry
from strawberry.types import Info

from typing import AsyncGenerator

from lms.api.v1 import fields, resolvers


@strawberry.type
class Query:
    """GraphQL query."""

    borrowers: list[fields.BorrowerOut] = strawberry.field(
        resolver=resolvers.get_borrowers,
    )

    borrower: fields.BorrowerOut = strawberry.field(
        resolver=resolvers.get_borrower,
    )

    borrower_loans: list[fields.LoanInformationOut] = strawberry.field(
        resolver=resolvers.get_borrower_loans,
    )

    loans_information: list[fields.LoanInformationOut] = strawberry.field(
        resolver=resolvers.get_loans_information,
    )

    loan_information: fields.LoanInformationOut = strawberry.field(
        resolver=resolvers.get_loan_information,
    )

    loan_information_payments: fields.PaymentOut = strawberry.field(
        resolver=resolvers.get_loan_information_payments,
    )

    loans_offers: list[fields.LoanOfferOut] = strawberry.field(
        resolver=resolvers.get_loans_offers,
    )

    loan_offer: fields.LoanOfferOut = strawberry.field(
        resolver=resolvers.get_loan_offer,
    )

    payments: list[fields.PaymentOut] = strawberry.field(
        resolver=resolvers.get_payments,
    )

    payment: fields.PaymentOut = strawberry.field(
        resolver=resolvers.get_payment,
    )

    reports: list[fields.ReportOut] = strawberry.field(
        resolver=resolvers.get_reports,
    )

    report: fields.ReportOut = strawberry.field(
        resolver=resolvers.get_report,
    )


@strawberry.type
class Mutation:
    """GraphQL mutation."""

    create_borrower: fields.BorrowerOut = (
        strawberry.mutation(
            resolver=resolvers.create_borrower,
        )
    )

    create_loan_information: fields.LoanInformationOut = (
        strawberry.mutation(
            resolver=resolvers.create_loan_information,
        )
    )


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
)
