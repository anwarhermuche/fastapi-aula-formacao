import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from ai.structured_outputs.posts import PostsStructuredOutput
from schemas.posts import PostInput
from services.openai_service import OpenAIService


def test_generate_output_openai_service(openai_service: OpenAIService):
    # Arrange
    post = PostInput(
        idea="Teste",
        communication_tone="Teste",
        target_audience="Teste",
        for_kids=False,
    )

    # Act
    output = openai_service.generate_output(post)

    # Assert
    assert output is not None
    assert output.title is not None
    assert type(output) == PostsStructuredOutput
