from controllers.controllers_adapter import user_controller
from fastapi import APIRouter
from models.user import User

user_router = APIRouter()

@user_router.get('/', response_model=list[User], response_model_exclude_none=True, status_code=200, tags=['users'])
async def get_users() -> list[User]:
    return user_controller.get_users()

@user_router.get('/{user_id}', response_model=User, response_model_exclude_none=True, status_code=200, tags=['users'])
async def get_user(user_id: int) -> User:
    return user_controller.get_user(user_id)

@user_router.patch('/{user_id}', response_model=User, status_code=200, tags=['users'])
async def update(user_id: int, user: User) -> User:
    return user_controller.update(user_id, user)

@user_router.delete('/{user_id}', status_code=200, tags=['users'])
async def delete(user_id: int):
    deleted_user = user_controller.delete(user_id)
    return {'message': 'deleted', 'user_id': deleted_user.id}
