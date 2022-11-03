"""Database utils."""

from beanie import init_beanie
from motor import motor_asyncio

from lms.database import models
from lms.settings import settings


async def init_database() -> motor_asyncio.AsyncIOMotorClient:
    """Initialize the database.
    Returns:
        AsyncIOMotorClient: database client.
    """
    client = motor_asyncio.AsyncIOMotorClient(settings.DATABASE_URL)
    print('client.get_default_database()', client.get_default_database())
    
    await init_beanie(
        database=client.get_default_database(),
        document_models=[models.Admin, models.Borrower, models.LoanInformation, models.Document, models.Payment,
                         models.LoanOffer],
    )
    return client
