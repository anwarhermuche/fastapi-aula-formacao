import pytest

from ..src.ai.structured_outputs.posts import PostsStructuredOutput
from ..src.services.openai_service import OpenAIService


@pytest.fixture
def openai_service():
    return OpenAIService(structured_output=PostsStructuredOutput)
