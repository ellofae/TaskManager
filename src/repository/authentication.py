from datetime import datetime

from database.database import session
from models.user import User, UserEntity, RegisterForm

def get_user(user_id: int) -> User:
    with session() as db:
        entity = db.query(UserEntity).get(user_id)
        assert entity, f'No user with id {user_id} exists'

        return User.from_entity(entity)

def create(register_form: RegisterForm) -> User:
    user_entity = UserEntity.from_model(register_form)
    user_entity.created_at = datetime.now()
    
    with session() as db:
        if user_entity.email:
            database_entity = db.query(UserEntity).filter(UserEntity.email == user_entity.email).first()
            assert not database_entity, 'Email is already registered'
        
        if user_entity.phone:
            database_entity = db.query(UserEntity).filter(UserEntity.phone == user_entity.phone).first()
            assert not database_entity, 'Phone number is already registered'
        

        return save(user_entity)
        
def save(entity: UserEntity) -> User:
    with session() as db:
        'False -> detect only local-column based properties'
        if db.is_modified(entity, include_collections=False):
            entity = db.merge(entity)
            
        db.add(entity)
        db.commit()
        return User.from_entity(entity)