"""App handlers."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from structlog import get_logger

from lms.api.router import graphql_router, graphql_app
from lms.api.v1.info import router as info_router
from lms.api.v1.borrower import router as borrower_router
from lms.database.client import init_database
from lms.settings import settings

logger = get_logger(__name__)


def create_application() -> FastAPI:
    """Create the FastAPI application.
    Returns:
        FastAPI: created panama.
    """

    logger.info("Creating lms...")
    _app_ = FastAPI(
        title=settings.TITLE,
        version=settings.VERSION,
        description=settings.DESCRIPTION,
        docs_url="/api/docs",
        on_startup=[init_database],
    )
    _app_.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["*"],
    )

    _app_.include_router(graphql_router, prefix="/graphql")
    _app_.add_websocket_route("/graphql", graphql_app)
    _app_.include_router(info_router, tags=["Root"])
    _app_.include_router(borrower_router, tags=["Borrower"], prefix="/borrower")
    return _app_


app = create_application()