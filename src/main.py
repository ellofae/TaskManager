from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

import common
from auth.jwt_auth import jwt_decode
from routers.authentication import authentication_router
from routers.refresh import refresh_router
from routers.user import user_router
from routers.task import task_router

origins = [
    "*"
]

@asynccontextmanager
async def lifespan(app: FastAPI):
    common.startup()
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

        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.lower().startswith('bearer'):
            return 'Bearer token is required'

        access_token = auth_header.split(' ')[1].strip()
        user_payload = jwt_decode(access_token)

        if not user_payload or not user_payload.get('user_id'):
            return 'Invalid token'

        request.state.user_id = user_payload.get('user_id')
        return None

    'if response is not None -> status code 401'
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
app.include_router(refresh_router, prefix='/refresh')
app.include_router(task_router, prefix='/tasks')