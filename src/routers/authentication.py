import services.authentication as service

from models.user import User
from fastapi import APIRouter

authentication_router = APIRouter()

@authentication_router.get('/', response_model=list[User], status_code=200, tags=['users'])
async def get_users() -> list[User]:
    return service.get_users()

@authentication_router.post('/', response_model=User, status_code=201, tags=['users'])
async def create(user: User) -> User:
    return service.create(user)