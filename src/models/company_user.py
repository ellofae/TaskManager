from typing import Optional
from datetime import date
from database.models_extensions import Base, BaseModelExtended
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

class CompanyUserEntity(Base):
    __tablename__ = 'company_users'

    id = Column(Integer, primary_key=True, index=True)
    user_status = Column(String, nullable=False, default='manager')
    company = Column(Integer, ForeignKey("companies.id", ondelete='CASCADE'), nullable=True)
    user = Column(Integer, ForeignKey("users.id", ondelete='CASCADE'), nullable=True)
    member_since = Column(DateTime, nullable=False)

class CompanyUser(BaseModelExtended):
    id: Optional[int] = None
    user_status: str
    member_since: str

    @classmethod
    def from_entity(cls, entity):
        return cls(**{key: value.strftime("%Y-%m-%d %H:%M:%S") if isinstance(value, date) else value for key, value in entity.to_dict().items()})

    class Config:
        orm_mode = True

class CompanyUserCreationForm(BaseModelExtended):
    user: int
    company: int
    user_status: str

    class Config:
        orm_mode = True