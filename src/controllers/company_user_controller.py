from models.company_user import CompanyUser
from models.company_status import CompanyStatus

from services.company_user_service import CompanyUserService
from repository.company_user_repository import CompanyUserRepository

class CompanyUserController:
    def __init__(self, cus: CompanyUserService):
        self.company_user_service = cus


def get_company_controller() -> CompanyUserController:
    company_user_repository = CompanyUserRepository()
    company_user_service = CompanyUserService(company_user_repository)

    return CompanyUserController(company_user_service)