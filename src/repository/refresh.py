import datetime

from database.database import session
from models.token import TokenEntity


def check_whether_exists(current_user_id: int) -> bool:
    with session() as db:
        entity = db.query(TokenEntity).filter(TokenEntity.user_id == current_user_id).first()
        if not entity:
            return False
        return True

def check_refresh_token(token: str, current_user_id: int) -> TokenEntity:
    with session() as db:
        entity = db.query(TokenEntity).filter(TokenEntity.user_id == current_user_id).first()
        assert entity.refresh_token == token, 'Invalid refresh token provided'

        return entity

def add_refresh_token(current_user_id: int, token: str, expiry: datetime):
    entity = TokenEntity(user_id=current_user_id, refresh_token=token, expiry=expiry)
    save(entity)

def update_refresh_token(entity: TokenEntity) -> None:
    save(entity)

def save(entity: TokenEntity):
    with session() as db:
        'False -> detect only local-column based properties'
        if db.is_modified(entity, include_collections=False):
            entity = db.merge(entity)

        db.add(entity)
        db.commit()