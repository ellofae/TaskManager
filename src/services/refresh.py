import repository.refresh as repo
import secrets
import string
import datetime

from decouple import config
from auth.jwt_auth import jwt_encode
from models.token import TokenResponse, RefreshToken, TokenEntity


def generate_refresh_token(length: int) -> str:
    characters = string.ascii_letters + string.digits
    refresh_token = ''.join(secrets.choice(characters) for _ in range(length))
    return refresh_token

def add_refresh_token(current_user_id: int) -> None:
    if repo.check_whether_exists(current_user_id):
        return

    expiry = datetime.datetime.now() + datetime.timedelta(hours=24)
    new_refresh_token = generate_refresh_token(int(config('REFRESH_TOKEN_LENGTH')))

    repo.add_refresh_token(current_user_id, new_refresh_token, expiry)

def refresh_token(token_model: RefreshToken, current_user_id: int) -> TokenResponse:
    entity = check_refresh_token(token_model.refresh_token, current_user_id)
    update_refresh_token(entity)

    access_token, expiry = jwt_encode(current_user_id)
    return TokenResponse(access_token=access_token, expiry=expiry)

def check_refresh_token(token: str, current_user_id: int) -> TokenEntity:
    return repo.check_refresh_token(token, current_user_id)

def update_refresh_token(entity: TokenEntity) -> None:
    entity.expiry = datetime.datetime.now() + datetime.timedelta(hours=24)
    entity.refresh_token = generate_refresh_token(int(config('REFRESH_TOKEN_LENGTH')))

    repo.update_refresh_token(entity)
