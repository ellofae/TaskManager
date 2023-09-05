from models.company import Company, CompanyEntity
from database.database import session

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