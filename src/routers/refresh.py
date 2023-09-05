from typing import Annotated

from common.current_user_data import get_current_user_id
from controllers.token_controller import get_token_controller
from fastapi import APIRouter, Depends
from models.token import RefreshToken

refresh_router = APIRouter()

@refresh_router.post('/', status_code=200, tags=['refresh'])
async def refresh_token(refresh_model: RefreshToken, current_user_id: Annotated[int, Depends(get_current_user_id)]):
    token_controller = get_token_controller()
    return token_controller.refresh_token(refresh_model, current_user_id)