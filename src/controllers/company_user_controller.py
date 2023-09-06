from models.company_user import CompanyUser

from repository.company_user_repository import CompanyUserRepository
from services.company_user_service import CompanyUserService


class CompanyUserController:
    def __init__(self, cus: CompanyUserService):
        self.company_user_service = cus

    def get_company_users(self, company_id: int, current_user_id: int) -> list[CompanyUser]:
        return self.company_user_service.get_company_users(company_id, current_user_id)


def get_company_user_controller() -> CompanyUserController:
    company_user_repository = CompanyUserRepository()
    company_user_service = CompanyUserService(company_user_repository)

    return CompanyUserController(company_user_service)