from models.token import TokenResponse
from models.user import User, IdentificationForm
from repository.token_repository import TokenRepository
from repository.user_repository import UserRepository
from services.token_service import TokenService
from services.user_service import UserService


class UserController:
    def __init__(self, us: UserService, ts: TokenService):
        self.user_service = us
        self.token_service = ts

    def login(self, user: IdentificationForm) -> TokenResponse:
        access_token_response, user_id = self.user_service.login(user)
        self.token_service.add_refresh_token(user_id)

        return access_token_response

    def create(self, user: IdentificationForm) -> User:
        return self.user_service.create(user)

    def get_users(self) -> list[User]:
        return self.user_service.get_users()

    def get_user(self, user_id: int) -> User:
        return self.user_service.get_user(user_id)

    def update(self, user_id: int, user: User) -> User:
        return self.user_service.update(user_id, user)

    def delete(self, user_id: int):
        return self.user_service.delete(user_id)

def get_user_controller() -> UserController:
    token_repository = TokenRepository()
    token_service = TokenService(token_repository)

    user_repository = UserRepository()
    user_service = UserService(user_repository)
    return UserController(user_service, token_service)