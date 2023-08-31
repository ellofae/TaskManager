import repository.user as repo

from database.database import session
from models.user import User, UserEntity, IdentificationForm


def get_users() -> list[User]:
    with session() as db:
        entities = db.query(UserEntity).order_by(UserEntity.id.desc()).all()
        return [User.from_entity(entity) for entity in entities]

def get_user(user_id: int) -> User:
    assert user_id > 0, 'User ID must be greater than zero'
    return repo.get_user(user_id)

def get_user_by_credentials(login_form: IdentificationForm) -> UserEntity:
    return repo.get_user_by_credentials(login_form)

def check_user_fields(user: User):
    repo.check_user_fields(user)

def update(user: User, user_id: int) -> User:
    assert user_id > 0, 'User ID must be greater than zero'
    check_user_fields(user)

    return repo.update(user, user_id)
