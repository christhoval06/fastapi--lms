"""App handlers."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from structlog import get_logger

from lms.auth.middleware.auth_middleware import AuthMiddleware
from lms.auth.deps import dependencies as auth_dependencies, verify_header
from lms.api.router import graphql_router, graphql_app
from lms.api.v1.info import router as info_router
# from lms.api.v1.borrower import router as borrower_router
from lms.database.client import init_database
from lms.settings import settings

logger = get_logger(__name__)


def create_application() -> FastAPI:
    """Create the FastAPI application.
    Returns:
        FastAPI: created panama.
    """

    logger.info("Creating lms...")
    lms_app = FastAPI(
        title=settings.TITLE,
        version=settings.VERSION,
        description=settings.DESCRIPTION,
        docs_url="/api/docs",
        on_startup=[init_database],
    )
    # lms_app.add_middleware(AuthMiddleware, verify_header=verify_header)
    lms_app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["*"],
    )

    lms_app.include_router(graphql_router, prefix="/graphql")
    # , dependencies=[*auth_dependencies])
    # lms_app.add_websocket_route("/graphql", graphql_app)
    lms_app.include_router(info_router, tags=["Root"])
    # lms_app.include_router(borrower_router, tags=["Borrower"], prefix="/borrower", dependencies=[*auth_dependencies])
    return lms_app


app = create_application()