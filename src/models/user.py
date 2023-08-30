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
    password = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    
class User(BaseModelExtended):
    id: Optional[int] = None
    email: Optional[str] = None
    phone: Optional[str] = Field(max_length=15, default=None)
    password: Optional[str] = Field(max_length=20, default=None)
    
    @classmethod
    def from_entity(cls, entity):
        entity_dict = entity.to_dict()
        entity_dict.pop('password')
        
        return cls(**entity_dict)
    
    class Config:
        orm_mode = True
