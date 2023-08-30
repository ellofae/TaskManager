from datetime import datetime
from models.user import User, UserEntity
from database.database import session

def create(user: User) -> User:
    user_entity = UserEntity.from_model(user)
    with session() as db:
        if user_entity.email:
            database_entity = db.query(UserEntity).filter(UserEntity.email == user_entity.email).first()
            assert not database_entity, 'Email is already registered'
        else:
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