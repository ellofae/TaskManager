import services.user as service
from fastapi import APIRouter
from models.token import TokenResponse
from models.user import User

user_router = APIRouter()

@user_router.get('/', response_model=list[User], response_model_exclude_none=True, status_code=200, tags=['users'])
async def get_users() -> list[User]:
    return service.get_users()

@user_router.get('/{user_id}', response_model=User, response_model_exclude_none=True, status_code=200, tags=['users'])
async def get_user(user_id: int) -> User:
    return service.get_user(user_id)

@user_router.patch('/{user_id}', response_model=User, status_code=200, tags=['users'])
async def update(user_id: int, user: User) -> User:
    return service.update(user, user_id)

@user_router.delete('/{user_id}', status_code=200, tags=['users'])
async def delete(user_id: int):
    deleted_user = service.delete(user_id)
    return {'message': 'deleted', 'user_id': deleted_user.id}
