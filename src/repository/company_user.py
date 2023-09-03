from datetime import datetime

from database.database import session
from models.company_status import CompanyStatus
from models.company_user import CompanyUser, CompanyUserEntity, CompanyUserUpdateForm


def get_company_user_by_id(company_user_id: int) -> CompanyUser:
    with session() as db:
        entity = db.query(CompanyUserEntity).get(company_user_id)
        assert entity, f'No company user with id {company_user_id} exists'

        return CompanyUser.from_entity(entity)

def get_company_users(company_id: int) -> list[CompanyUser]:
    with session() as db:
        entities = db.query(CompanyUserEntity).filter(CompanyUserEntity.company == company_id).order_by(CompanyUserEntity.id.desc()).all()
        return [CompanyUser.from_entity(entity) for entity in entities]

def get_current_company_user(company_id: int, current_user_id: int) -> CompanyUser:
    with session() as db:
        entity = db.query(CompanyUserEntity).filter(CompanyUserEntity.company == company_id, CompanyUserEntity.user == current_user_id).first()
        assert entity, f'User with id {current_user_id} is not registered for the company with id {company_id}'
        return CompanyUser.from_entity(entity)

def get_allowed_companies(current_user_id) -> list[int]:
    with session() as db:
        company_ids = db.query(CompanyUserEntity.id).filter(CompanyUserEntity.user == current_user_id).order_by(CompanyUserEntity.id.desc()).all()
        return company_ids

def check_weather_user_exists(user_id: int, company_id: int) -> CompanyUser | None:
    with session() as db:
        entity = db.query(CompanyUserEntity).filter(CompanyUserEntity.user == user_id, CompanyUserEntity.company == company_id).first()
        if not entity:
            return None

        return CompanyUser.from_entity(entity)

def attach_user(user_id: int, company_id: int, company_status: CompanyStatus) -> CompanyUser:
    with session() as db:
        company_user = db.query(CompanyUserEntity).filter(CompanyUserEntity.company == company_id, CompanyUserEntity.user == user_id).first()
        assert not company_user, f'User with id {user_id} is already registered for company with id {company_id}'

    entity = CompanyUserEntity(company=company_id, user=user_id, member_since=datetime.now(), user_status=company_status)
    return save(entity)

def update(company_user_id: int, company_user: CompanyUserUpdateForm) -> CompanyUser:
    with session() as db:
        entity = db.query(CompanyUserEntity).get(company_user_id)
        assert entity, f'No company user with id {company_user_id} exists'

        for key, value in company_user.dict(exclude_unset=True).items():
            setattr(entity, key, value)

        entity.updated_at = datetime.now()
        return save(entity)

def delete(company_user_id: int) -> CompanyUser:
    with session() as db:
        entity = db.query(CompanyUserEntity).get(company_user_id)
        assert entity, f'No task with id {company_user_id} exists'

        db.delete(entity)
        db.commit()

        return CompanyUser.from_entity(entity)

def save(entity: CompanyUserEntity) -> CompanyUser:
    with session() as db:
        if db.is_modified(entity, include_collections=False):
            entity = db.merge(entity)

        db.add(entity)
        db.commit()
        return CompanyUser.from_entity(entity)