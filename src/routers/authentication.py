import services.authentication as service
from fastapi import APIRouter
from models.user import User, IdentificationForm
from models.token_response import TokenResponse

authentication_router = APIRouter()

@authentication_router.get('/', response_model=list[User], response_model_exclude_none=True, status_code=200, tags=['users'])
async def get_users() -> list[User]:
    return service.get_users()

@authentication_router.get('/{user_id}', response_model=User, response_model_exclude_none=True, status_code=200, tags=['users'])
async def get_user(user_id: int) -> User:
    return service.get_user(user_id)

@authentication_router.post('/', response_model=User, response_model_exclude_none=True, status_code=201, tags=['users'])
async def create(register_form: IdentificationForm) -> User:
    return service.create(register_form)

@authentication_router.post('/login', status_code=200, tags=['users'])
async def login(login_form: IdentificationForm):
    token_data = service.login(login_form)
    return {'token_data': token_data}

@authentication_router.patch('/{user_id}', status_code=200, tags=['users'])
async def update(user: User, user_id: int) -> TokenResponse:
    return service.update(user, user_id)
