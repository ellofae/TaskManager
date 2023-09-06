from database.models_extensions import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class UserTask(Base):
    __tablename__ = 'user_tasks'

    user_id = Column(Integer, ForeignKey('company_users.id'), primary_key=True)
    task_id = Column(Integer, ForeignKey('tasks.id'), primary_key=True)

    user = relationship("CompanyUserEntity", backref="user_tasks")
    task = relationship("TaskEntity", backref="user_tasks")
