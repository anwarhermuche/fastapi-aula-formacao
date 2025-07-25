from datetime import datetime

from pydantic import (
    BaseModel,
    Field,
)


class Post(BaseModel):
    title: str
    content: str
    keywords: str
    created_at: datetime = datetime.now()


class PostResponse(Post):
    id: int


class PostInput(BaseModel):
    idea: str = Field(
        min_length=3, max_length=100, description="Ideia da publicação"
    )
    communication_tone: str = Field(min_length=3, max_length=100)
    target_audience: str = Field(min_length=3, max_length=100)
    for_kids: bool = Field(default=False)
