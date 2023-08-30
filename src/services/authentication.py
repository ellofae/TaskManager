import repository.authentication as repo
import services.hashing as hashing_service
from database.database import session
from models.user import User, UserEntity, IdentificationForm


def get_users() -> list[User]:
    with session() as db:
        entities = db.query(UserEntity).order_by(UserEntity.id.desc()).all()
        return [User.from_entity(entity) for entity in entities]

def get_user(user_id: int) -> User:
    assert user_id > 0, 'User ID must be greater than zero'
    return repo.get_user(user_id)

def create(register_form: IdentificationForm) -> User:
    register_form.password = hashing_service.password_hashing(register_form.password)
    return repo.create(register_form)

def update(user: User, user_id: int) -> User:
    assert user_id > 0, 'User ID must be greater than zero'
    return repo.update(user, user_id)
