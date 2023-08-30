import repository.authentication as repo

from models.user import User, UserEntity
from database.database import session

def get_users() -> list[User]:
    with session() as db:
        entities = db.query(UserEntity).order_by(UserEntity.id.desc()).all()
        return [User.from_model(entity) for entity in entities]

def create(user: User) -> User:
    return repo.create(user)