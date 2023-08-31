from models.company_user import CompanyUser, CompanyUserEntity
from database.database import session
from datetime import datetime

def check_weather_user_exists(user_id: int, company_id: int) -> None:
    with session() as db:
        entity = db.query(CompanyUserEntity).filter(CompanyUserEntity.user == user_id, CompanyUserEntity.company == company_id).first()
        assert not entity, f'User with id {user_id} is already registered for the company with id {company_id}'

def attach_user(user_id: int, company_id: int) -> None:
    entity = CompanyUserEntity(company=company_id, user=user_id, member_since=datetime.now())
    with session() as db:
        save(entity)

def save(entity: CompanyUserEntity) -> CompanyUser:
    with session() as db:
        if db.is_modified(entity, include_collections=False):
            entity = db.merge(entity)

        db.add(entity)
        db.commit()
        return CompanyUser.from_entity(entity)