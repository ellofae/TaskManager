from models.company_user import CompanyUser, CompanyUserEntity
from models.company_status import CompanyStatus
from database.database import session
from datetime import datetime

class CompanyUserRepository:
    # Command module
    def save(self, entity: CompanyUserEntity) -> CompanyUser:
        with session() as db:
            'False -> detect only local-column based properties'
            if db.is_modified(entity, include_collections=False):
                entity = db.merge(entity)

            db.add(entity)
            db.commit()

            return CompanyUser.from_entity(entity)

    def attach_user(self, user_id: int, company_id: int, company_status: CompanyStatus) -> CompanyUser:
        entity = CompanyUserEntity(company=company_id, user=user_id, member_since=datetime.now(), user_status=company_status)
        return self.save(entity)

    # Querying module
    def check_weather_user_exists(self, user_id: int, company_id: int) -> CompanyUser | None:
        with session() as db:
            entity = db.query(CompanyUserEntity).filter(CompanyUserEntity.user == user_id,
                                                        CompanyUserEntity.company == company_id).first()
            if not entity:
                return None

            return CompanyUser.from_entity(entity)