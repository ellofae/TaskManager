from datetime import datetime

from database.database import session
from models.user import User, UserEntity, IdentificationForm


def get_user(user_id: int) -> User:
    with session() as db:
        entity = db.query(UserEntity).get(user_id)
        assert entity, f'No user with id {user_id} exists'

        return User.from_entity(entity)

def update(user: User, user_id: int) -> User:
    with session() as db:
        user_to_update = db.query(UserEntity).get(user_id)
        assert user_to_update, f'No user with id {user_id} exists'

        if user.email:
            assert user_to_update.email != user.email, 'You cannot change your email to the one you already have'

        assert user_to_update.phone != user.phone, 'You cannot change your phone to the one you already have'

        for key, value in user.dict(exclude_unset=True).items():
            setattr(user_to_update, key, value)

        user_to_update.updated_at = datetime.now()
        return save(user_to_update)

def get_user_by_credentials(login_form: IdentificationForm) -> UserEntity:
    with session() as db:
        if login_form.email:
            entity = db.query(UserEntity).filter(UserEntity.email == login_form.email).first()
            assert entity, 'No user with such email exists'
        elif login_form.phone:
            entity = db.query(UserEntity).filter(UserEntity.phone == login_form.phone).first()
            assert entity, 'No user with such phone exists'

        return entity


def check_user_fields(user: User) -> None:
    with session() as db:
        if user.email:
            database_entity = db.query(UserEntity).filter(UserEntity.email == user.email).first()
            assert not database_entity, 'Email is already registered'

        if user.phone:
            database_entity = db.query(UserEntity).filter(UserEntity.phone == user.phone).first()
            assert not database_entity, 'Phone number is already registered'

def delete(user_id: int) -> User:
    with session() as db:
        entity = db.query(UserEntity).get(user_id)
        assert entity, f'No user with id {user_id} exists'

        db.delete(entity)
        db.commit()

        return User.from_entity(entity)

def save(entity: UserEntity) -> User:
    with session() as db:
        'False -> detect only local-column based properties'
        if db.is_modified(entity, include_collections=False):
            entity = db.merge(entity)
            
        db.add(entity)
        db.commit()
        return User.from_entity(entity)