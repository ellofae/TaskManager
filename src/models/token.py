from database.models_extensions import BaseModelExtended, Base
from sqlalchemy import Column, Integer, String, DateTime

class TokenEntity(Base):
    __tablename__ = 'tokens'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    refresh_token = Column(String, nullable=True)
    expiry = Column(DateTime, nullable=True)

class TokenResponse(BaseModelExtended):
    'Response model to the sign in action'
    access_token: str
    expiry: str

class RefreshToken(BaseModelExtended):
    'Request model to the refresh action'
    refresh_token: str