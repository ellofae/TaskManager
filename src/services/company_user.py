import repository.company_user as repo
from models.company_user import CompanyUser

def check_weather_user_exists(user_id: int, company_id: int) -> None:
    repo.check_weather_user_exists(user_id, company_id)

def attach_user(user_id: int, company_id: int) -> None:
    check_weather_user_exists(user_id, company_id)
    repo.attach_user(user_id, company_id)