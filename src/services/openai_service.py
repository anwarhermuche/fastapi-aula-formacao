from typing import List, Optional, Union

from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from pydantic import BaseModel

from ai.prompts.generate_post_prompt import (
    GENERATE_POST_PROMPT_ADULT,
    GENERATE_POST_PROMPT_KIDS,
)
from schemas.posts import PostInput

load_dotenv()


class OpenAIService:
    def __init__(
        self,
        model: str = "gpt-4.1-mini",
        temperature: float = 0.1,
        structured_output: Optional[BaseModel] = None,
    ):
        self.__llm = ChatOpenAI(model=model, temperature=temperature)
        self.__structured_output = structured_output

    def __generate_prompt(self, post: PostInput) -> List[BaseMessage]:
        messages = [
            SystemMessage(
                content=GENERATE_POST_PROMPT_ADULT
                if not post.for_kids
                else GENERATE_POST_PROMPT_KIDS
            )
        ]

        human_message = HumanMessage(
            content=f"""
        Ideia do post: {post.idea}
        Tom de comunicação: {post.communication_tone}
        Público alvo: {post.target_audience}
        """
        )

        messages.append(human_message)

        return messages

    def generate_output(self, post: PostInput) -> Union[BaseModel, str]:
        prompt = self.__generate_prompt(post)
        if self.__structured_output:
            return self.__llm.with_structured_output(
                self.__structured_output
            ).invoke(prompt)
        else:
            return self.__llm.invoke(prompt).content