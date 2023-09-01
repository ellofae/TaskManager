import repository.company_user as repo
from models.company_user import CompanyUser

def get_user_by_company_id(company_id: int, current_user_id: int):
    return repo.get_user_by_company_id(company_id, current_user_id)

def get_allowed_companies(current_user_id) -> list[int]:
    return repo.get_allowed_companies(current_user_id)

def check_weather_user_exists(user_id: int, company_id: int) -> None:
    repo.check_weather_user_exists(user_id, company_id)

def attach_user(user_id: int, company_id: int) -> None:
    check_weather_user_exists(user_id, company_id)
    repo.attach_user(user_id, company_id)