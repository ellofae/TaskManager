from datetime import date
from typing import Optional

from database.models_extensions import Base, BaseModelExtended
from pydantic import Field
from sqlalchemy import Column, Integer, String, DateTime

class TaskEntity(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    task_specifications = Column(String, nullable=False)
    status = Column(String, nullable=False, default='active')
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)

class Task(BaseModelExtended):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    task_specifications: str

    class Config:
        orm_mode = True
