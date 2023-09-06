from controllers.controllers_adapter import user_controller
from fastapi import APIRouter
from models.user import User, IdentificationForm

authentication_router = APIRouter()

@authentication_router.post('/register', response_model=User, response_model_exclude_none=True, status_code=201, tags=['authentication'])
async def create(register_form: IdentificationForm) -> User:
    return user_controller.create(register_form)

@authentication_router.post('/login', status_code=200, tags=['authentication'])
async def login(login_form: IdentificationForm):
    token_data = user_controller.login(login_form)
    return {'token_data': token_data}