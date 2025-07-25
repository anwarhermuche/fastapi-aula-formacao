from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from src.crud.posts import PostsCRUD
from src.db.engine import get_db
from src.schemas.posts import PostInput, PostResponse

posts_router = APIRouter(prefix="/api/v1/posts", tags=["posts"])


@posts_router.get(
    "/", response_model=List[PostResponse], status_code=HTTPStatus.OK
)
def get_all_posts(db: Session = Depends(get_db)):
    return PostsCRUD(db).get_all_posts()


@posts_router.get(
    "/{id}", response_model=PostResponse, status_code=HTTPStatus.OK
)
def get_post_by_id(id: int, db: Session = Depends(get_db)):
    publicacao = PostsCRUD(db).get_post_by_id(id)
    if publicacao:
        return publicacao

    raise HTTPException(status_code=404, detail="Post not found")


@posts_router.post(
    "/", response_model=PostResponse, status_code=HTTPStatus.CREATED
)
def create_post(post: PostInput, db: Session = Depends(get_db)):
    return PostsCRUD(db).create_post(post)


@posts_router.put(
    "/{id}", response_model=PostResponse, status_code=HTTPStatus.OK
)
def update_post(id: int, post: PostInput, db: Session = Depends(get_db)):
    post_to_update = PostsCRUD(db).get_post_by_id(id)
    if post_to_update:
        return PostsCRUD(db).update_post(id, post)

    raise HTTPException(status_code=404, detail="Post not found")


@posts_router.delete("/{id}", status_code=HTTPStatus.NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    post_to_delete = PostsCRUD(db).get_post_by_id(id)
    if post_to_delete:
        PostsCRUD(db).delete_post(id)
        return Response(status_code=HTTPStatus.NO_CONTENT)

    raise HTTPException(status_code=404, detail="Post not found")
