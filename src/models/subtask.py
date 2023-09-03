from datetime import date
from typing import Optional

from database.models_extensions import Base, BaseModelExtended
from pydantic import Field
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


class SubtaskEntity(Base):
    __tablename__ = 'subtasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    task_specifications = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)

    created_by = Column(Integer, ForeignKey("company_users.id", ondelete='CASCADE'), nullable=False)
    task = Column(Integer, ForeignKey("tasks.id", ondelete='CASCADE'), nullable=True)

class Subtask(BaseModelExtended):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    task_specifications: str
    task: int
    created_by: int
    created_at: str

    @classmethod
    def from_entity(cls, entity):
        return cls(**{key: value.strftime("%Y-%m-%d %H:%M:%S") if isinstance(value, date) else value for key, value in
                      entity.to_dict().items()})
    class Config:
        orm_mode = True

class SubtaskCreationForm(BaseModelExtended):
    title: str
    description: Optional[str] = None
    task_specifications: str
    task: int = Field(gt=0)

    class Config:
        orm_mode = True

class SubtaskUpdateForm(BaseModelExtended):
    title: Optional[str] = None
    description: Optional[str] = None
    task_specifications: Optional[str] = None

    class Config:
        orm_mode = True