import init_settings

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.authentication import authentication_router


origins = [
    "*"
]

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_settings.startup()
    yield


app = FastAPI(
    title = 'TaskManagerAPI',
    description = "API that helps managing user's tasks",
    lifespan = lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(authentication_router, prefix='/authentication')