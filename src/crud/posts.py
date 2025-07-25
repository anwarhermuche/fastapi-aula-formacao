from datetime import datetime

from sqlalchemy.orm import Session

from ai.structured_outputs.posts import PostsStructuredOutput
from models.posts import Posts
from schemas.posts import PostInput
from services.openai_service import OpenAIService

openai_service = OpenAIService(structured_output=PostsStructuredOutput)


class PostsCRUD:
    def __init__(self, db: Session):
        self.__db = db

    def get_all_posts(self):
        return self.__db.query(Posts).all()

    def get_post_by_id(self, id: int):
        return self.__db.query(Posts).filter(Posts.id == id).first()

    def create_post(self, post: PostInput):
        post_output = openai_service.generate_output(post)

        new_post = Posts(
            title=post_output.title,
            content=post_output.content,
            keywords=post_output.keywords,
        )

        self.__db.add(new_post)
        self.__db.commit()
        self.__db.refresh(new_post)
        return new_post

    def update_post(self, id: int, new_post: PostInput):
        post_to_update = self.get_post_by_id(id)

        post_output = openai_service.generate_output(new_post)

        post_to_update.title = post_output.title
        post_to_update.content = post_output.content
        post_to_update.keywords = post_output.keywords
        post_to_update.created_at = datetime.now()

        self.__db.commit()
        self.__db.refresh(post_to_update)
        return post_to_update

    def delete_post(self, id: int):
        post_to_delete = self.get_post_by_id(id)
        self.__db.delete(post_to_delete)
        self.__db.commit()
        return True
