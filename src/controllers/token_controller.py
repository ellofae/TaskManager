from models.token import TokenResponse, RefreshToken
from repository.token_repository import TokenRepository
from services.token_service import TokenService


class TokenController:
    def __init__(self, ts: TokenService):
        self.token_service = ts

    def refresh_token(self, refresh_model: RefreshToken, current_user_id: int) -> TokenResponse:
        return self.token_service.refresh_token(refresh_model, current_user_id)


def get_token_controller() -> TokenController:
    token_repository = TokenRepository()
    token_service = TokenService(token_repository)
    return TokenController(token_service)