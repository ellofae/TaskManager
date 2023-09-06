from models.company_user import CompanyUser, CompanyUserCreationForm, CompanyUserUpdateForm
from models.company_status import CompanyStatus

from repository.company_user_repository import CompanyUserRepository
from services.company_user_service import CompanyUserService


class CompanyUserController:
    def __init__(self, cus: CompanyUserService):
        self.company_user_service = cus

    def create(self, company_user: CompanyUserCreationForm, current_user_id: int) -> CompanyUser:
        return self.company_user_service.create(company_user, current_user_id)

    def update(self, company_user_id: int, company_user: CompanyUserUpdateForm, current_user_id: int) -> CompanyUser:
        return self.company_user_service.update(company_user_id, company_user, current_user_id)

    def get_company_user_by_id(self, company_user_id: int, current_user_id: int) -> CompanyUser:
        return self.company_user_service.get_company_user_by_id(company_user_id, current_user_id)

    def get_company_users(self, company_id: int, current_user_id: int) -> list[CompanyUser]:
        return self.company_user_service.get_company_users(company_id, current_user_id)


def get_company_user_controller() -> CompanyUserController:
    company_user_repository = CompanyUserRepository()
    company_user_service = CompanyUserService(company_user_repository)

    return CompanyUserController(company_user_service)