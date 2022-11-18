import strawberry
from strawberry.types import Info

from typing import AsyncGenerator

from lms.auth.Is_authenticated import IsAuthenticated
from lms.api.v1 import fields, resolvers


@strawberry.type
class Query:
    """GraphQL query."""

    borrowers: list[fields.BorrowerOut] = strawberry.field(
        resolver=resolvers.get_borrowers,
        permission_classes=[IsAuthenticated]
    )

    borrower: fields.BorrowerOut = strawberry.field(
        resolver=resolvers.get_borrower,
        permission_classes=[IsAuthenticated]
    )

    borrower_loans: list[fields.LoanInformationOut] = strawberry.field(
        resolver=resolvers.get_borrower_loans,
        permission_classes=[IsAuthenticated]
    )

    loans_information: list[fields.LoanInformationOut] = strawberry.field(
        resolver=resolvers.get_loans_information,
        # permission_classes=[IsAuthenticated]
    )

    loan_information: fields.LoanInformationOut = strawberry.field(
        resolver=resolvers.get_loan_information,
        permission_classes=[IsAuthenticated]
    )

    loan_information_payments: fields.PaymentOut = strawberry.field(
        resolver=resolvers.get_loan_information_payments,
        permission_classes=[IsAuthenticated]
    )

    loans_offers: list[fields.LoanOfferOut] = strawberry.field(
        resolver=resolvers.get_loans_offers,
        # permission_classes=[IsAuthenticated]
    )

    loan_offer: fields.LoanOfferOut = strawberry.field(
        resolver=resolvers.get_loan_offer,
        permission_classes=[IsAuthenticated]
    )

    payments: list[fields.PaymentOut] = strawberry.field(
        resolver=resolvers.get_payments,
        # permission_classes=[IsAuthenticated]
    )

    payment: fields.PaymentOut = strawberry.field(
        resolver=resolvers.get_payment,
        permission_classes=[IsAuthenticated]
    )

    reports: list[fields.ReportOut] = strawberry.field(
        resolver=resolvers.get_reports,
        # permission_classes=[IsAuthenticated]
    )

    report: fields.ReportOut = strawberry.field(
        resolver=resolvers.get_report,
        permission_classes=[IsAuthenticated]
    )


@strawberry.type
class Mutation:
    """GraphQL mutation."""

    create_user: fields.AdminOut = (
        strawberry.mutation(
            resolver=resolvers.create_user,
            # permission_classes=[IsAuthenticated]
        )
    )

    auth_login: fields.LoginSuccess = (
        strawberry.mutation(
            resolver=resolvers.user_login,
        )
    )

    create_borrower: fields.BorrowerOut = (
        strawberry.mutation(
            resolver=resolvers.create_borrower,
            permission_classes=[IsAuthenticated]
        )
    )

    create_loan_information: fields.LoanInformationOut = (
        strawberry.mutation(
            resolver=resolvers.create_loan_information,
            permission_classes=[IsAuthenticated]
        )
    )


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
)
