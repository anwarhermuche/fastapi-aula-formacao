from fastapi import FastAPI
from routes.api.v1.posts import posts_router

app = FastAPI()

app.include_router(posts_router)