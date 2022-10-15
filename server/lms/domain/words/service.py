"""Model logic for the words domain."""

import uuid

from structlog import get_logger

from panama.api.v1 import fields
from panama.domain.repositories import generic

logger = get_logger(__name__)


class WordService:
    """Orchestrator for the words domain.
    Contains the business logic around the words model operations.
    """

    def __init__(self, repository: generic.Repository) -> None:
        self.repository = repository

    async def create(
        self,
        data_object: fields.WordCreate,
    ) -> fields.WordOut:
        """Create a new word.
        Args:
            data_object (WordCreate): input data.
        Returns:
            WordOut: representation of the created word.
        """
        logger.info("Creating word", data=data_object)
        logger.info("Creating word", data=data_object)
        word = await self.repository.create(data_object)
        logger.info("Created word", entry=word)
        return word

    async def get_by_id(self, pk: uuid.UUID) -> fields.WordOut:
        """Get a word by its ID.
        Args:
            pk (UUID): word ID.
        Returns:
            WordOut: representation of the word.
        """
        logger.info("Getting word", id=pk)
        word = await self.repository.get_by_id(pk)
        logger.info("Got word by ID", entry=word)
        return word

    async def collect(self) -> list[fields.WordOut]:
        """Collect all words.
        Returns:
            list[WordOut]: list of words.
        """
        logger.info("Collecting words")
        words = await self.repository.collect()
        logger.info("Collected words", qty=len(words))
        return words

    async def delete(self, pk: uuid.UUID) -> None:
        """Delete a word.
        Args:
            pk (UUID): word ID.
        """
        logger.info("Deleting word", id=pk)
        await self.repository.delete(pk)
        logger.info("Deleted word", id=pk)

    async def update(
        self,
        pk: uuid.UUID,
        data_object: fields.WordUpdate,
    ) -> fields.WordOut:
        """Update a word.
        Args:
            pk (UUID): word ID.
            data_object (WordUpdate): input data.
        Returns:
            WordOut: updated word.
        """
        logger.info("Updating word", id=pk, data=data_object)
        word = await self.repository.update(pk, data_object)
        logger.info("Updated word", entry=word)
        return word

    async def update_many(
        self,
        ids: list[uuid.UUID],
        data_object: fields.WordUpdate,
    ) -> list[fields.WordOut]:
        """Update many words.
        Args:
            ids (list[UUID]): list of word IDs.
            data_object (WordUpdate): input data.
        Returns:
            list[WordOut]: list of updated words.
        """
        logger.info("Updating words", ids=ids, data=data_object)
        words = await self.repository.update_many(ids, data_object)
        logger.info("Updated words", qty=len(words))
        return words