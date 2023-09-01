import services.company as service
from common.current_user_data import get_current_user_id

from typing import Annotated
from models.company import Company
from fastapi import APIRouter, Depends

company_router = APIRouter()

@company_router.get('/', response_model=list[Company], response_model_exclude_none=True, status_code=200, tags=['companies'])
async def get_all_companies(current_user_id: Annotated[int, Depends(get_current_user_id)]) -> list[Company]:
    return service.get_all_companies(current_user_id)

@company_router.get('/{company_id}', response_model=Company, response_model_exclude_none=True, status_code=200, tags=['companies'])
async def get_company_by_id(company_id: int, current_user_id: Annotated[int, Depends(get_current_user_id)]) -> list[Company]:
    return service.get_company_by_id(company_id, current_user_id)

@company_router.post('/', response_model=Company, response_model_exclude_none=True, status_code=201, tags=['companies'])
async def create(company: Company, current_user_id: Annotated[int, Depends(get_current_user_id)]) -> Company:
    return service.create(company, current_user_id)