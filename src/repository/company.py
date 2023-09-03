from datetime import datetime

from database.database import session
from models.company import Company, CompanyEntity


def get_company_by_id(company_id: int) -> Company:
    with session() as db:
        entity = db.query(CompanyEntity).get(company_id)
        assert entity, f'No company with id {company_id} exists'

        return Company.from_entity(entity)

def get_all_companies(company_ids: list[int]) -> list[CompanyEntity]:
    with session() as db:
        entities = []
        for id in company_ids:
            entities.append(db.query(CompanyEntity).get(id))

        return entities

def create(company: Company):
    entity = CompanyEntity.from_model(company)
    entity.created_at = datetime.now()
    return save(entity)

def save(entity: CompanyEntity) -> Company:
    with session() as db:
        if db.is_modified(entity, include_collections=False):
            entity = db.merge(entity)

        db.add(entity)
        db.commit()
        return Company.from_entity(entity)