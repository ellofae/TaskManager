import utils.hashing as hashing_util

from datetime import datetime

from models.user import IdentificationForm, User, UserEntity
from models.token import TokenResponse

from auth.jwt_auth import jwt_encode
from repository.user_repository import UserRepository

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def login(self, user: IdentificationForm) -> (TokenResponse, int):
        user_entity = self.repo.get_user_by_credentials(user)
        assert hashing_util.password_compare(user.password, user_entity.password), 'Incorrect password'

        access_token, expiry = jwt_encode(user_entity.id)
        return TokenResponse(access_token=access_token, expiry=expiry), user_entity.id

    def create(self, user: IdentificationForm) -> User:
        user.password = hashing_util.password_hashing(user.password)
        self.repo.check_user_fields(user)

        user_entity = UserEntity.from_model(user)
        user_entity.created_at = datetime.now()

        return self.repo.save(user_entity)

    def get_users(self) -> list[User]:
        return self.repo.get_users()

    def get_user(self, user_id: int) -> User:
        assert user_id > 0, 'User id must be greater than zero'
        return self.repo.get_user(user_id)


    def update(self, user_id: int, user: User) -> User:
        assert user_id > 0, 'User id must be greater than zero'
        self.repo.check_user_fields(user)

        user_to_update = self.repo.get_user_entity(user_id)
        assert user_to_update, f'No user with id {user_id} exists'

        return self.repo.update(user, user_to_update)

    def delete(self, user_id: int) -> User:
        assert user_id > 0, 'User id must be greater than zero'

        user_to_delete = self.repo.get_user_entity(user_id)
        assert user_to_delete, f'No user with id {user_id} exists'

        return self.repo.delete(user_to_delete)

    def check_user_fields(self, user: IdentificationForm) -> None:
        self.repo.check_user_fields(user)