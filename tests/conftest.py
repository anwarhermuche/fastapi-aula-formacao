from ai.structured_outputs.posts import PostsStructuredOutput
from services.openai_service import OpenAIService
import pytest


@pytest.fixture
def openai_service():
    return OpenAIService(structured_output=PostsStructuredOutput)
