from datetime import datetime
from models.token import TokenResponse, RefreshToken, TokenEntity
from database.database import session

class TokenRepository:
    # Command module
    def save(self, entity: TokenEntity):
        with session() as db:
            'False -> detect only local-column based properties'
            if db.is_modified(entity, include_collections=False):
                entity = db.merge(entity)

            db.add(entity)
            db.commit()

    # Querying module
    def check_refresh_token(self, token: str, current_user_id: int) -> TokenEntity:
        with session() as db:
            entity = db.query(TokenEntity).filter(TokenEntity.user_id == current_user_id).first()
            assert entity.refresh_token == token, 'Invalid refresh token provided'

            return entity

    def check_whether_exists(self, user_id: int) -> bool:
        with session() as db:
            entity = db.query(TokenEntity).filter(TokenEntity.user_id == user_id).first()

            if not entity:
                return False
            return True