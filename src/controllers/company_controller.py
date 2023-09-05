from models.company import Company
from models.company_status import CompanyStatus

from services.company_user_service import CompanyUserService
from services.company_service import CompanyService

from repository.company_repository import CompanyRepository
from repository.company_user_repository import CompanyUserRepository

class CompanyController:
    def __init__(self, cs: CompanyService, cus: CompanyUserService):
        self.company_service = cs
        self.company_user_service = cus

    def get_company_by_id(self, company_id: int, current_user_id) -> Company:
        company = self.company_service.get_company_by_id(company_id)

        current_company_user = self.company_user_service.check_weather_user_exists(current_user_id, company_id)
        assert current_company_user, f'User with id {current_user_id} is not registered for the company with id {company_id}'
        
        return company

    def create(self, company: Company, current_user_id: int) -> Company:
        company = self.company_service.create(company)
        self.company_user_service.attach_user(current_user_id, company.id, CompanyStatus.MANAGER)
        return company


def get_company_controller() -> CompanyController:
    company_user_repository = CompanyUserRepository()
    company_user_service = CompanyUserService(company_user_repository)

    company_repository = CompanyRepository()
    company_service = CompanyService(company_repository)

    return CompanyController(company_service, company_user_service)