from datetime import date, datetime
from typing import Optional
from pydantic import Field
from database.models_extensions import Base, BaseModelExtended
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

class SubtaskEntity(Base):
    __tablename__ = 'subtasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    task_specifications = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)

    task = Column(Integer, ForeignKey("tasks.id", ondelete='CASCADE'), nullable=True)

class Subtask(BaseModelExtended):
    id: Optional[int] = None
    title: str
    description: Optional[str]
    task_specifications: str
    created_at: str

    @classmethod
    def from_entity(cls, entity):
        return cls(**{key: value.strftime("%Y-%m-%d %H:%M:%S") if isinstance(value, date) else value for key, value in
                      entity.to_dict().items()})
    class Config:
        orm_mode = True

class SubtaskCreationForm(BaseModelExtended):
    title: str
    description: Optional[str]
    task_specifications: str
    task: int = Field(gt=0)

    class Config:
        orm_mode = True