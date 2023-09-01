import repository.company as repo
import services.company_user as company_user_service
from models.company import Company, CompanyEntity
from models.company_status import CompanyStatus
from models.company_user import CompanyUserEntity, CompanyUser
from database.database import session

def get_company_users(company_id: int, current_user_id: int) -> list[CompanyUser]:
    assert company_id > 0, 'Company id must be grater than zero'
    return company_user_service.get_company_users(company_id, current_user_id)

def get_company_by_id(company_id: int, current_user_id: int) -> Company:
    assert company_id > 0, 'Company id must be greater than zero'
    company_user_service.get_current_company_user(company_id, current_user_id)
    return repo.get_company_by_id(company_id)

def get_all_companies(current_user_id: int) -> list[Company]:
    company_ids_user_attached_to = company_user_service.get_allowed_companies(current_user_id)
    company_entities = repo.get_all_companies(company_ids_user_attached_to)
    return [Company.from_entity(entity) for entity in company_entities]

def create(company: Company, current_user_id: int) -> Company:
    company = repo.create(company)
    company_user_service.attach_user(current_user_id, company.id, CompanyStatus.MANAGER)
    return company