from typing import Annotated

from common.current_user_data import get_current_user_id
from controllers.controllers_adapter import company_controller, task_controller, company_user_controller
from fastapi import APIRouter, Depends
from models.company import Company
from models.company_user import CompanyUser
from models.task import Task

company_router = APIRouter()

@company_router.get('/', response_model=list[Company], response_model_exclude_none=True, status_code=200, tags=['companies'])
async def get_all_companies(current_user_id: Annotated[int, Depends(get_current_user_id)]) -> list[Company]:
    return company_controller.get_all_companies(current_user_id)

@company_router.get('/{company_id}/tasks', response_model=list[Task], response_model_exclude_none=True, status_code=200, tags=['companies'])
async def get_all_tasks(company_id: int, current_user_id: Annotated[int, Depends(get_current_user_id)]) -> list[Task]:
    return task_controller.get_all_tasks(company_id, current_user_id)

@company_router.get('/{company_id}/users', response_model=list[CompanyUser], response_model_exclude_none=True, status_code=200, tags=['companies'])
async def get_company_users(company_id: int, current_user_id: Annotated[int, Depends(get_current_user_id)]) -> list[CompanyUser]:
    return company_user_controller.get_company_users(company_id, current_user_id)

@company_router.get('/{company_id}', response_model=Company, response_model_exclude_none=True, status_code=200, tags=['companies'])
async def get_company_by_id(company_id: int, current_user_id: Annotated[int, Depends(get_current_user_id)]) -> list[Company]:
    return company_controller.get_company_by_id(company_id, current_user_id)

@company_router.post('/', response_model=Company, response_model_exclude_none=True, status_code=201, tags=['companies'])
async def create(company: Company, current_user_id: Annotated[int, Depends(get_current_user_id)]) -> Company:
    return company_controller.create(company, current_user_id)