from datetime import datetime
from models.company import Company, CompanyEntity

from repository.company_repository import CompanyRepository

class CompanyService:
    def __init__(self, repo: CompanyRepository):
        self.repo = repo

    def get_company_by_id(self, company_id: int) -> Company:
        assert company_id > 0, 'Company id must be greater than zero'
        return self.repo.get_company_by_id(company_id)

    def create(self, company: Company) -> Company:
        entity = CompanyEntity.from_model(company)
        entity.created_at = datetime.now()

        return self.repo.save(entity)