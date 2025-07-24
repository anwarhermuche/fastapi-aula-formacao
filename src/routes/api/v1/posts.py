from fastapi import APIRouter

posts_router = APIRouter(prefix = "/api/v1/posts", tags = ["posts"])

@posts_router.get("/")
def get_posts():
    return {"message": "Tem muitos caios"}