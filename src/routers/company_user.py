from typing import Annotated

from common.current_user_data import get_current_user_id
from fastapi import APIRouter, Depends
from models.company_user import CompanyUser, CompanyUserCreationForm, CompanyUserUpdateForm

company_user_router = APIRouter()

from controllers.controllers_adapter import company_user_controller

@company_user_router.get('/{company_user_id}', response_model=CompanyUser, response_model_exclude_none=True, status_code=200, tags=['company_users'])
async def get_company_user_by_id(company_user_id: int, current_user_id: Annotated[int, Depends(get_current_user_id)]) -> CompanyUser:
    return company_user_controller.get_company_user_by_id(company_user_id, current_user_id)

@company_user_router.post('/', response_model=CompanyUser, response_model_exclude_none=True, status_code=201, tags=['company_users'])
async def create(company_user: CompanyUserCreationForm, current_user_id: Annotated[int, Depends(get_current_user_id)]) -> CompanyUser:
    return company_user_controller.create(company_user, current_user_id)

@company_user_router.patch('/{company_user_id}', response_model=CompanyUser, response_model_exclude_none=True, status_code=200, tags=['company_users'])
async def update(company_user_id: int, company_user: CompanyUserUpdateForm, current_user_id: Annotated[int, Depends(get_current_user_id)]) -> CompanyUser:
    return company_user_controller.update(company_user_id, company_user, current_user_id)

@company_user_router.delete('/{company_user_id}', status_code=200, tags=['company_users'])
async def delete(company_user_id: int, current_user_id: Annotated[int, Depends(get_current_user_id)]):
    company_user_deleted = company_user_controller.delete(company_user_id, current_user_id)
    return {'message': 'company user deleted', 'company user id': company_user_deleted.id}