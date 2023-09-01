import services.company_user as service

from fastapi import APIRouter, Depends
from models.company_user import CompanyUser, CompanyUserCreationForm
from typing import Annotated
from common.current_user_data import get_current_user_id

company_user_router = APIRouter()

# @company_user_router.get('/{company_user_id}', response_model=CompanyUser, response_model_exclude_none=True, status_code=200, tags=['company_users'])
# async def get_company_user_by_id(company_user_id: int, current_user_id: Annotated[int, Depends(get_current_user_id)]) -> CompanyUser:
#     return get_company_user_by_id(company_user_id, current_user_id)

@company_user_router.post('/', response_model=CompanyUser, response_model_exclude_none=True, status_code=201, tags=['company_users'])
async def create(company_user: CompanyUserCreationForm, current_user_id: Annotated[int, Depends(get_current_user_id)]) -> CompanyUser:
    return service.create(company_user, current_user_id)