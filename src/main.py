from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

import init_settings
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

@app.exception_handler(AssertionError)
async def uvicorn_exception_handler(request: Request, exc: AssertionError):
    return JSONResponse(
        status_code = 400,
        content = {'message': str(exc)}
    )

@app.exception_handler(Exception)
async def uvicorn_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code = 500,
        content = {'message': 'Something went wrong!'}
    )

app.include_router(authentication_router, prefix='/authentication')