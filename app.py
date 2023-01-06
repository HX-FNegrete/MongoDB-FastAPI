from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="REST API with FastAPI & MongoDB",
    description="This is a Rest Api using FastAPI and MongoDB for Bootcamp pourpose",
    version="0.0.1",
)

app.include_router(user)
