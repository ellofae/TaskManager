from datetime import date, datetime
from typing import Optional

from database.models_extensions import Base, BaseModelExtended
from pydantic import Field
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class TaskEntity(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    task_specifications = Column(String, nullable=False)
    deadline = Column(DateTime, nullable=True)
    status = Column(String, nullable=False, default='active')
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)

    created_by = Column(Integer, ForeignKey("company_users.id", ondelete='CASCADE'), nullable=True)
    company_id = Column(Integer, ForeignKey("companies.id", ondelete='CASCADE'), nullable=True)

    'Relationships'
    company_user = relationship("CompanyUserEntity")
    company = relationship("CompanyEntity")

class Task(BaseModelExtended):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    task_specifications: str
    deadline: Optional[str] = None
    created_by: int
    company_id: int
    status: str
    created_at: str

    @classmethod
    def from_entity(cls, entity):
        return cls(**{key: value.strftime("%Y-%m-%d %H:%M:%S") if isinstance(value, date) else value for key, value in entity.to_dict().items()})

    class Config:
        orm_mode = True

class TaskCreationForm(BaseModelExtended):
    description: Optional[str] = None
    task_specifications: str
    deadline: Optional[datetime] = None
    company_id: int = Field(gt=0)

    class Config:
        orm_mode = True

    title: str


class TaskUpdateForm(BaseModelExtended):
    title: Optional[str] = None
    description: Optional[str] = None
    task_specifications: Optional[str] = None
    status: Optional[str] = None

    class Config:
        orm_mode = True