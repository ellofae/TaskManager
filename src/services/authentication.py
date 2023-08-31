import repository.authentication as repo
import services.hashing as hashing_service
import services.user as user_service
import services.refresh as refresh_service

from auth.jwt_auth import jwt_encode
from models.user import User, UserEntity, IdentificationForm
from models.token import TokenResponse

def create(register_form: IdentificationForm) -> User:
    register_form.password = hashing_service.password_hashing(register_form.password)

    return repo.create(register_form)

def login(login_form: IdentificationForm) -> TokenResponse:
    user_entity = user_service.get_user_by_credentials(login_form)
    assert hashing_service.password_compare(login_form.password, user_entity.password), 'Incorrect password'

    refresh_service.add_refresh_token(user_entity.id)

    access_token, expiry = jwt_encode(user_entity.id)
    return TokenResponse(access_token = access_token, expiry = expiry)