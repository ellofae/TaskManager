import services.refresh as service

from fastapi import APIRouter, Depends
from models.token import TokenResponse, RefreshToken
from common.current_user_data import get_current_user_id
from typing import Annotated

refresh_router = APIRouter()

@refresh_router.post('/', status_code=200, tags=['refresh'])
async def refresh_token(refresh_model: RefreshToken, current_user_id: Annotated[int, Depends(get_current_user_id)]):
    return service.refresh_token(refresh_model, current_user_id)