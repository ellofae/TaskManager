from datetime import datetime

from database.database import session
from models.user import User, UserEntity, IdentificationForm

def get_user(user_id: int) -> User:
    with session() as db:
        entity = db.query(UserEntity).get(user_id)
        assert entity, f'No user with id {user_id} exists'

        return User.from_entity(entity)

def create(register_form: IdentificationForm) -> User:
    user_entity = UserEntity.from_model(register_form)
    user_entity.created_at = datetime.now()
    
    check_user_fields(user_entity)
    return save(user_entity)

def update(user: User, user_id: int) -> User:
    with session() as db:
        user_to_update = db.query(UserEntity).get(user_id)
        assert user_to_update, f'No user with id {user_id} exists'

        assert user_to_update.email != user.email, 'You cannot change your email to the one you already have'
        assert user_to_update.phone != user.phone, 'You cannot change your phone to the one you already have'

        check_user_fields(user)
        for key, value in user.dict(exclude_unset=True).items():
            setattr(user_to_update, key, value)

        return save(user_to_update)

def check_user_fields(entity: UserEntity):
    with session() as db:
        if entity.email:
            database_entity = db.query(UserEntity).filter(UserEntity.email == entity.email).first()
            assert not database_entity, 'Email is already registered'

        if entity.phone:
            database_entity = db.query(UserEntity).filter(UserEntity.phone == entity.phone).first()
            assert not database_entity, 'Phone number is already registered'
        
def save(entity: UserEntity) -> User:
    with session() as db:
        'False -> detect only local-column based properties'
        if db.is_modified(entity, include_collections=False):
            entity = db.merge(entity)
            
        db.add(entity)
        db.commit()
        return User.from_entity(entity)