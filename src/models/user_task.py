from database.models_extensions import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

# UserTask = Table('user_task', Base.metadata,
#     Column('user_id', Integer, ForeignKey('users.id')),
#     Column('task_id', Integer, ForeignKey('tasks.id'))
# )
#

class UserTask(Base):
    __tablename__ = 'user_tasks'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    task_id = Column(Integer, ForeignKey('tasks.id'), primary_key=True)

    user = relationship("UserEntity", backref="user_tasks")
    task = relationship("TaskEntity", backref="user_tasks")
