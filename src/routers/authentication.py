import services.authentication as service
from fastapi import APIRouter
from models.user import User, RegisterForm

authentication_router = APIRouter()

@authentication_router.get('/', response_model=list[User], response_model_exclude_none=True, status_code=200, tags=['users'])
async def get_users() -> list[User]:
    return service.get_users()

@authentication_router.get('/{user_id}', response_model=User, response_model_exclude_none=True, status_code=200, tags=['users'])
async def get_user(user_id: int) -> User:
    return service.get_user(user_id)

@authentication_router.post('/', response_model=User, response_model_exclude_unset=True, status_code=201, tags=['users'])
async def create(register_form: RegisterForm) -> User:
    return service.create(register_form)

