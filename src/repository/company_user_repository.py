from datetime import datetime

from database.database import session
from models.company_status import CompanyStatus
from models.company_user import CompanyUser, CompanyUserEntity


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

    def delete(self, entity: CompanyUserEntity) -> CompanyUser:
        with session() as db:
            db.delete(entity)
            db.commit()

            return CompanyUser.from_entity(entity)

    def attach_user(self, user_id: int, company_id: int, company_status: CompanyStatus) -> CompanyUser:
        entity = CompanyUserEntity(company=company_id, user=user_id, member_since=datetime.now(), user_status=company_status)
        return self.save(entity)

    # Querying module
    def get_company_user_entity_by_id(self, company_user_id: int) -> CompanyUserEntity:
        with session() as db:
            entity = db.query(CompanyUserEntity).get(company_user_id)
            assert entity, f'No company user with id {company_user_id} exists'

            return entity

    def get_company_user_by_id(self, company_user_id: int) -> CompanyUser:
        with session() as db:
            entity = db.query(CompanyUserEntity).get(company_user_id)
            assert entity, f'No company user with id {company_user_id} exists'

            return CompanyUser.from_entity(entity)

    def get_company_users(self, company_id: int) -> list[CompanyUser]:
        with session() as db:
            entities = db.query(CompanyUserEntity).filter(CompanyUserEntity.company == company_id).order_by(
                CompanyUserEntity.id.desc()).all()
            return [CompanyUser.from_entity(entity) for entity in entities]

    def check_weather_user_exists(self, user_id: int, company_id: int) -> CompanyUser | None:
        with session() as db:
            entity = db.query(CompanyUserEntity).filter(CompanyUserEntity.user == user_id,
                                                        CompanyUserEntity.company == company_id).first()
            if not entity:
                return None

            return CompanyUser.from_entity(entity)

    def get_allowed_companies(self, user_id: int) -> list[int]:
        with session() as db:
            company_ids = db.query(CompanyUserEntity.id).filter(CompanyUserEntity.user == user_id).order_by(
                CompanyUserEntity.id.desc()).all()
            return company_ids