from fastapi import APIRouter
from models.company_user import CompanyUser

company_user_router = APIRouter()

# @company_user_router.get('/', response_model=list[CompanyUser])