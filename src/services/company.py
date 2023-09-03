import repository.company as repo
import services.company_user as company_user_service
import services.task as task_service
from models.company import Company
from models.company_status import CompanyStatus
from models.company_user import CompanyUser
from models.task import Task


def get_all_tasks(company_id: int, current_user_id: int) -> list[Task]:
    company_user = company_user_service.check_weather_user_exists(current_user_id, company_id)
    return task_service.get_all_tasks(company_user.id)

def get_company_users(company_id: int, current_user_id: int) -> list[CompanyUser]:
    assert company_id > 0, 'Company id must be grater than zero'
    return company_user_service.get_company_users(company_id, current_user_id)

def get_company_by_id(company_id: int, current_user_id: int) -> Company:
    assert company_id > 0, 'Company id must be greater than zero'

    company_user_service.check_weather_user_exists(current_user_id, company_id)
    return repo.get_company_by_id(company_id)

def get_all_companies(current_user_id: int) -> list[Company]:
    company_ids_user_attached_to = company_user_service.get_allowed_companies(current_user_id)
    company_entities = repo.get_all_companies(company_ids_user_attached_to)
    return [Company.from_entity(entity) for entity in company_entities]

def create(company: Company, current_user_id: int) -> Company:
    company = repo.create(company)
    company_user_service.attach_user(current_user_id, company.id, CompanyStatus.MANAGER)
    return company