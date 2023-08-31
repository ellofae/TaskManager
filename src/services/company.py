import repository.company as repo
import services.company_user as company_user_service
from models.company import Company, CompanyEntity

def create(company: Company, current_user_id: int) -> Company:
    company = repo.create(company)
    company_user_service.attach_user(current_user_id, company.id)
    return company