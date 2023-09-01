from models.company import Company, CompanyEntity
from database.database import session

def get_company_by_id(company_id: int) -> Company:
    with session() as db:
        entity = db.query(CompanyEntity).get(company_id)
        assert entity, f'No company with id {company_id} exists'

        return Company.from_entity(entity)

def get_all_companies(comany_ids: int) -> list[CompanyEntity]:
    with session() as db:
        entities = []
        for id in comany_ids:
            entities.append(db.query(CompanyEntity).get(id))

        return entities

def create(company: Company):
    entity = CompanyEntity.from_model(company)
    return save(entity)

def save(entity: CompanyEntity) -> Company:
    with session() as db:
        if db.is_modified(entity, include_collections=False):
            entity = db.merge(entity)

        db.add(entity)
        db.commit()
        return Company.from_entity(entity)