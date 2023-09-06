from datetime import date
from typing import Optional

from database.models_extensions import Base, BaseModelExtended
from models.company_status import CompanyStatus
from pydantic import Field
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Enum


class CompanyUserEntity(Base):
    __tablename__ = 'company_users'

    id = Column(Integer, primary_key=True, index=True)
    user_status = Column(Enum(CompanyStatus), nullable=False, default=CompanyStatus.MANAGER)
    company = Column(Integer, ForeignKey("companies.id", ondelete='CASCADE'), nullable=True)
    user = Column(Integer, ForeignKey("users.id", ondelete='CASCADE'), nullable=True)
    member_since = Column(DateTime, nullable=False)

class CompanyUser(BaseModelExtended):
    id: Optional[int] = None
    user_status: CompanyStatus
    member_since: str
    company: int

    @classmethod
    def from_entity(cls, entity):
        return cls(**{key: value.strftime("%Y-%m-%d %H:%M:%S") if isinstance(value, date) else value for key, value in entity.to_dict().items()})

    class Config:
        orm_mode = True

class CompanyUserCreationForm(BaseModelExtended):
    user: int = Field(gt=0)
    company: int = Field(gt=0)
    user_status: CompanyStatus

    class Config:
        orm_mode = True

class CompanyUserUpdateForm(BaseModelExtended):
    user_status: Optional[CompanyStatus]
    class Config:
        orm_mode = True