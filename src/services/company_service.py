from datetime import datetime
from models.company import Company, CompanyEntity

from repository.company_repository import CompanyRepository

class CompanyService:
    def __init__(self, repo: CompanyRepository):
        self.repo = repo

    def create(self, company: Company) -> Company:
        entity = CompanyEntity.from_model(company)
        entity.created_at = datetime.now()

        return self.repo.save(entity)