"""GraphQL routing."""

from fastapi import FastAPI, Depends, Request, WebSocket, BackgroundTasks
from strawberry.fastapi import GraphQLRouter, BaseContext
from strawberry.asgi import GraphQL

from lms.api.schema import schema

from lms.domain.borrowers.registry import borrowers_registry
from lms.domain.loan_information.registry import loan_informations_registry


class CustomContext(BaseContext):
    def __init__(self):
        super(CustomContext, self).__init__()
        self.borrowers_srv = borrowers_registry.service
        self.linfo_srv = loan_informations_registry.service


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
