import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from ai.structured_outputs.posts import PostsStructuredOutput
from services.openai_service import OpenAIService


@pytest.fixture
def openai_service():
    return OpenAIService(structured_output=PostsStructuredOutput)
