from datetime import date, datetime
from typing import Optional

from database.models_extensions import Base, BaseModelExtended
from pydantic import Field
from sqlalchemy import Column, Integer, String, DateTime

class TaskEntity(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    task_specifications = Column(String, nullable=False)
    deadline = Column(DateTime, nullable=True)
    status = Column(String, nullable=False, default='active')
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)

class Task(BaseModelExtended):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    task_specifications: str
    deadline: Optional[str] = None
    status: str
    created_at: str

    @classmethod
    def from_entity(cls, entity):
        return cls(**{key: value.strftime("%Y-%m-%d %H:%M:%S") if isinstance(value, date) else value for key, value in entity.to_dict().items()})

    class Config:
        orm_mode = True

class TaskCreationForm(BaseModelExtended):
    title: str
    description: Optional[str] = None
    task_specifications: str
    deadline: Optional[datetime] = None

    class Config:
        orm_mode = True

class TaskUpdateForm(BaseModelExtended):
    title: Optional[str] = None
    description: Optional[str] = None
    task_specifications: Optional[str] = None
    status: Optional[str] = None

    class Config:
        orm_mode = True