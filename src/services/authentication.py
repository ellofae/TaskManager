import repository.authentication as repo
import services.hashing as hashing_service
from database.database import session
from models.user import User, UserEntity


def get_users() -> list[User]:
    with session() as db:
        entities = db.query(UserEntity).order_by(UserEntity.id.desc()).all()
        return [User.from_entity(entity) for entity in entities]

def create(user: User) -> User:
    user.password = hashing_service.password_hashing(user.password)
    return repo.create(user)