from typing import Optional
from datetime import datetime

from pydantic import Field
from database.models_extensions import Base, BaseModelExtended
from sqlalchemy import Column, Integer, String, DateTime

class UserEntity(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=True)
    
class User(BaseModelExtended):
    id: Optional[str] = None
    email: Optional[str] = None
    phone: str = Field(max_length=15)
    
    class Config:
        orm_mode = True
