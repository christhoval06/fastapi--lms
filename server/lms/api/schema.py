import strawberry
from strawberry.types import Info

from typing import AsyncGenerator

from lms.api.v1 import fields, resolvers


@strawberry.type
class Query:
    """GraphQL query."""

    borrower: fields.BorrowerOut = strawberry.field(
        resolver=resolvers.get_borrower,
    )

    borrowers: list[fields.BorrowerOut] = strawberry.field(
        resolver=resolvers.get_borrowers,
    )

    loans_information: list[fields.LoanInformationOut] = strawberry.field(
        resolver=resolvers.get_loans_information,
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
