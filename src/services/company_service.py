from datetime import datetime

from models.company import Company, CompanyEntity
from repository.company_repository import CompanyRepository


class CompanyService:
    def __init__(self, repo: CompanyRepository):
        self.repo = repo

    def get_company_by_id(self, company_id: int) -> Company:
        assert company_id > 0, 'Company id must be greater than zero'
        return self.repo.get_company_by_id(company_id)

    def get_all_companies(self, companies_ids: list[int]) -> list[Company]:
        companies = self.repo.get_all_companies(companies_ids)
        return [Company.from_entity(entity) for entity in companies]

    def create(self, company: Company) -> Company:
        entity = CompanyEntity.from_model(company)
        entity.created_at = datetime.now()

        return self.repo.save(entity)