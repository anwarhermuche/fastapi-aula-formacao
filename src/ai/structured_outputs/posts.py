from pydantic import BaseModel, Field


class PostsStructuredOutput(BaseModel):
    title: str = Field(description="Título do post")
    content: str = Field(description="Conteúdo do post")
    keywords: str = Field(
        description="4 palavras-chave do post separadas por vírgula"
    )
