"""Set of pre-instantiated dependencies for the words domain."""

from panama.domain.words.repository import WordsOdmRepository
from panama.domain.words.service import WordService


class WordsRegistry:
    """Registry of dependencies for the words domain."""

    service = WordService(repository=WordsOdmRepository())


words_registry = WordsRegistry()
