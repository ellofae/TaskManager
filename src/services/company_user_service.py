from datetime import datetime

from models.company_status import CompanyStatus
from models.company_user import CompanyUser, CompanyUserCreationForm, CompanyUserUpdateForm, CompanyUserEntity
from repository.company_user_repository import CompanyUserRepository


class CompanyUserService:
    def __init__(self, repo: CompanyUserRepository):
        self.repo = repo

    def create(self, company_user: CompanyUserCreationForm, current_user_id: int) -> CompanyUser:
        current_user = self.check_weather_user_exists_wrapper(current_user_id, company_user.company)
        assert current_user.user_status == CompanyStatus.MANAGER, 'Only manager can add new users to the company'

        self.check_weather_user_exists_wrapper(company_user.user, company_user.company)

        return self.repo.attach_user(company_user.user, company_user.company, company_user.user_status)

    def update(self, company_user_id: int, company_user: CompanyUserUpdateForm, current_user_id: int) -> CompanyUser:
        assert company_user_id > 0, 'Company user id must be greater than zero'
        company_user_to_update = self.repo.get_company_user_by_id(company_user_id)

        self.check_weather_user_exists_wrapper(current_user_id, company_user_to_update.company)

        entity = CompanyUserEntity.from_model(company_user_to_update)
        for key, value in company_user.dict(exclude_unset=True).items():
            setattr(entity, key, value)

        entity.updated_at = datetime.now()

        return self.repo.save(entity)

    def delete(self, company_user_id: int, current_user_id) -> CompanyUser:
        assert company_user_id > 0, "Company user id must be greater than zero"

        company_user_entity_to_delete = self.repo.get_company_user_entity_by_id(company_user_id)
        self.check_weather_user_exists_wrapper(current_user_id, company_user_entity_to_delete.company)

        return self.repo.delete(company_user_entity_to_delete)

    def get_company_user_by_id(self, company_user_id: int, current_user_id: int) -> CompanyUser:
        assert company_user_id > 0, 'Company user id must be greater than zero'
        company_user = self.repo.get_company_user_by_id(company_user_id)

        self.check_weather_user_exists_wrapper(current_user_id, company_user.company)

        return company_user

    def get_company_users(self, company_id: int, user_id: int) -> list[CompanyUser]:
        self.check_weather_user_exists_wrapper(user_id, company_id)

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

    def check_weather_user_exists_wrapper(self, user_id: int, company_id: int) -> CompanyUser:
        company_user = self.check_weather_user_exists(user_id, company_id)
        assert company_user, f'User with id {user_id} is already registered for company with id {company_id}'

        return company_user