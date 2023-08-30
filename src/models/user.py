from typing import Optional
from datetime import datetime, date

from database.models_extensions import Base, BaseModelExtended
from pydantic import Field
from sqlalchemy import Column, Integer, String, DateTime


class UserEntity(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=True)
    password = Column(String, nullable=False)
    status = Column(String, nullable=False, default='user')
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)
    
class User(BaseModelExtended):
    id: Optional[int] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[str] = None

    @classmethod
    def from_entity(cls, entity):
        return cls(**{key: value.strftime("%Y-%m-%d %H:%M:%S") if isinstance(value, date) else value for key, value in entity.to_dict().items()})
    
    class Config:
        orm_mode = True

class IdentificationForm(BaseModelExtended):
    email: Optional[str] = None
    phone: str = Field(max_length=15) #Optional[str] = Field(max_length=15, default=None)
    password: str = Field(max_length=20)

    class Config:
        orm_mode = True
