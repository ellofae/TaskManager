import repository.company_user as repo
from models.company_status import CompanyStatus
from models.company_user import CompanyUser, CompanyUserCreationForm

def get_company_user_by_id(company_user_id: int, current_user_id: int) -> CompanyUser:
    assert company_user_id > 0, 'Company user id must be greater than zero'
    company_user = repo.get_company_user_by_id(company_user_id)
    # TODO: only the one who is attached to the same company get get the attached user
    #repo.get_current_company_user(company_user.company, current_user_id)
    
    return company_user

def get_company_users(company_id: int, current_user_id: int) -> list[CompanyUser]:
    repo.get_current_company_user(company_id, current_user_id)
    return repo.get_company_users(company_id)
    

def create(company_user: CompanyUserCreationForm, current_user_id: int) -> CompanyUser:
    current_user = repo.get_current_company_user(company_user.company, current_user_id)
    assert current_user.user_status == CompanyStatus.MANAGER, 'Only manager can add new users to the company'

    return repo.attach_user(company_user.user, company_user.company, company_user.user_status)

def get_current_company_user(company_id: int, current_user_id: int):
    return repo.get_current_company_user(company_id, current_user_id)

def get_allowed_companies(current_user_id) -> list[int]:
    return repo.get_allowed_companies(current_user_id)

def check_weather_user_exists(user_id: int, company_id: int) -> CompanyUser:
    return repo.check_weather_user_exists(user_id, company_id)

def attach_user(user_id: int, company_id: int, company_status: CompanyStatus) -> None:
    company_user = check_weather_user_exists(user_id, company_id)
    assert not company_user, f'User with id {user_id} is already registered for the company with id {company_id}'

    repo.attach_user(user_id, company_id, company_status)