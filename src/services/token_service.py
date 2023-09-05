import datetime
import utils.token_generation as token_util

from auth.jwt_auth import jwt_encode
from decouple import config
from repository.token_repository import TokenRepository
from models.token import TokenResponse, RefreshToken, TokenEntity

class TokenService:
    def __init__(self, repo: TokenRepository):
        self.repo = repo

    def refresh_token(self, refresh_model: RefreshToken, current_user_id: int) -> TokenResponse:
        entity = self.repo.check_refresh_token(refresh_model.refresh_token, current_user_id)

        entity.expiry = datetime.datetime.now() + datetime.timedelta(hours=24)
        entity.refresh_token = token_util.generate_refresh_token(int(config('REFRESH_TOKEN_LENGTH')))

        self.repo.save(entity)

        access_token, expiry = jwt_encode(current_user_id)
        return TokenResponse(access_token=access_token, expiry=expiry)

    def add_refresh_token(self, user_id: int) -> None:
        if self.repo.check_whether_exists(user_id):
            return

        expiry = datetime.datetime.now() + datetime.timedelta(hours=24)
        new_refresh_token = token_util.generate_refresh_token(int(config('REFRESH_TOKEN_LENGTH')))

        entity = TokenEntity(user_id=user_id, refresh_token=new_refresh_token, expiry=expiry)
        self.repo.save(entity)