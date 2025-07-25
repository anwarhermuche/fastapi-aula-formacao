import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from fastapi import FastAPI

from routes.api.v1.posts import (
    posts_router,
)

app = FastAPI()

app.include_router(posts_router)
