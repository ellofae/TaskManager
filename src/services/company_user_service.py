from models.company_status import CompanyStatus
from models.company_user import CompanyUser
from repository.company_user_repository import CompanyUserRepository


class CompanyUserService:
    def __init__(self, repo: CompanyUserRepository):
        self.repo = repo

    def get_company_user_by_id(self, company_user_id: int, current_user_id: int) -> CompanyUser:
        assert company_user_id > 0, 'Company user id must be greater than zero'
        company_user = self.repo.get_company_user_by_id(company_user_id)

        current_user = self.repo.check_weather_user_exists(current_user_id, company_user.company)
        assert current_user, f'User with id {current_user_id} is not registered for the company with id {company_user.company}'

        return company_user

    def get_company_users(self, company_id: int, user_id: int) -> list[CompanyUser]:
        current_company_user = self.repo.check_weather_user_exists(user_id, company_id)
        assert current_company_user, f'User with id {user_id} is already registered for company with id {company_id}'

        return self.repo.get_company_users(company_id)

    def get_allowed_companies(self, user_id: int) -> list[int]:
        return self.repo.get_allowed_companies(user_id)

    def check_weather_user_exists(self, user_id: int, company_id: int) -> CompanyUser | None:
        assert company_id > 0, 'Company id must be greater than zero'
        return self.repo.check_weather_user_exists(user_id, company_id)

    def attach_user(self, user_id: int, company_id: int, company_status: CompanyStatus) -> None:
        user_to_check = self.repo.check_weather_user_exists(user_id, company_id)
        assert not user_to_check, f'User with id {user_id} is already registered for company with id {company_id}'

        self.repo.attach_user(user_id, company_id, company_status)
