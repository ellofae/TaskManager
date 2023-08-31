from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

import init_settings
from routers.user import user_router
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

@app.middleware("http")
async def authentication(request: Request, call_next):
    def auth() -> str | None:
        if request.method == 'GET' and request.url.path[1:] in ['docs', 'redoc', 'openapi.json', 'favicon.ico']:
            return None

        if request.url.path.startswith('/auth'):
            return None

        if request.url.path.startswith('/static'):
            return None

        return None

    'if response not is not None -> status code 401'
    if auth_error := auth():
        return JSONResponse(status_code=401, content={'message': auth_error})

    response = await call_next(request)
    return response

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(user_router, prefix='/users')
app.include_router(authentication_router, prefix='/authentication')