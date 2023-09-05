from models.company_user import CompanyUser
from models.company_status import CompanyStatus

from repository.company_user_repository import CompanyUserRepository

class CompanyUserService:
    def __init__(self, repo: CompanyUserRepository):
        self.repo = repo

    def get_allowed_companies(self, user_id: int) -> list[int]:
        return self.repo.get_allowed_companies(user_id)

    def check_weather_user_exists(self, user_id: int, company_id: int) -> CompanyUser | None:
        return self.repo.check_weather_user_exists(user_id, company_id)

    def attach_user(self, user_id: int, company_id: int, company_status: CompanyStatus) -> None:
        user_to_check = self.repo.check_weather_user_exists(user_id, company_id)
        assert not user_to_check, f'User with id {user_id} is already registered for company with id {company_id}'

        self.repo.attach_user(user_id, company_id, company_status)
