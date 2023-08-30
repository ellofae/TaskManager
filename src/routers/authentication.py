import services.authentication as service
from fastapi import APIRouter
from models.user import User

authentication_router = APIRouter()

@authentication_router.get('/', response_model=list[User], response_model_exclude_unset=True, status_code=200, tags=['users'])
async def get_users() -> list[User]:
    return service.get_users()

@authentication_router.post('/', response_model=User, response_model_exclude_unset=True, status_code=201, tags=['users'])
async def create(user: User) -> User:
    return service.create(user)