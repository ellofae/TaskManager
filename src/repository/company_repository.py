from database.database import session
from models.company import Company, CompanyEntity


class CompanyRepository:
    # Command module
    def save(self, entity: CompanyEntity) -> Company:
        with session() as db:
            'False -> detect only local-column based properties'
            if db.is_modified(entity, include_collections=False):
                entity = db.merge(entity)

            db.add(entity)
            db.commit()

            return Company.from_entity(entity)

    # Querying module
    def get_company_by_id(self, company_id: int) -> Company:
        with session() as db:
            entity = db.query(CompanyEntity).get(company_id)
            assert entity, f'No company with id {company_id} exists'

            return Company.from_entity(entity)

    def get_all_companies(self, companies_ids: list[int]) -> list[CompanyEntity]:
        with session() as db:
            entities = []
            for id in companies_ids:
                entities.append(db.query(CompanyEntity).get(id))

            return entities