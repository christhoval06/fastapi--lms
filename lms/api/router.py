"""GraphQL routing."""

from fastapi import FastAPI, Depends, Request, WebSocket, BackgroundTasks
from strawberry.fastapi import GraphQLRouter, BaseContext
from strawberry.asgi import GraphQL

from lms.api.schema import schema

from lms.domain import borrowers_srv, linfo_srv, payments_srv, loan_offer_srv, reports_srv, users_srv


class CustomContext(BaseContext):
    def __init__(self):
        super(CustomContext, self).__init__()
        self.borrowers_srv = borrowers_srv
        self.linfo_srv = linfo_srv
        self.payments_srv = payments_srv
        self.loan_offer_srv = loan_offer_srv
        self.reports_srv = reports_srv
        self.users_srv = users_srv


def custom_context_dependency() -> CustomContext:
    return CustomContext()


async def get_context(
        custom_context=Depends(custom_context_dependency),
):
    return custom_context


graphql_router = GraphQLRouter(
    schema,
    context_getter=get_context, )
graphql_app = GraphQL(schema)
