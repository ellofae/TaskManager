from datetime import datetime

from database.database import session
from models.user import User, UserEntity, IdentificationForm


def create(register_form: IdentificationForm) -> User:
    user_entity = UserEntity.from_model(register_form)
    user_entity.created_at = datetime.now()

    check_user_fields(user_entity)
    return save(user_entity)

def check_user_fields(user: UserEntity) -> None:
    with session() as db:
        if user.email:
            database_entity = db.query(UserEntity).filter(UserEntity.email == user.email).first()
            assert not database_entity, 'Email is already registered'

        if user.phone:
            database_entity = db.query(UserEntity).filter(UserEntity.phone == user.phone).first()
            assert not database_entity, 'Phone number is already registered'

def save(entity: UserEntity) -> User:
    with session() as db:
        'False -> detect only local-column based properties'
        if db.is_modified(entity, include_collections=False):
            entity = db.merge(entity)

        db.add(entity)
        db.commit()
        return User.from_entity(entity)