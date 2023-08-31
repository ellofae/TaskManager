from models.company import Company, CompanyEntity
from database.database import session

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