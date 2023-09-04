from datetime import datetime

from database.database import session
from models.task import Task, TaskEntity, TaskCreationForm, TaskUpdateForm
from models.user_task import UserTask


def get_task_by_id(task_id: int) -> Task:
    with session() as db:
        entity = db.query(TaskEntity).get(task_id)
        assert entity, f'No task with id {task_id} exists'

        return Task.from_entity(entity)

def create(task: TaskCreationForm, company_user_id: int) -> Task:
    entity = TaskEntity.from_model(task)
    entity.created_by = company_user_id
    entity.created_at = datetime.now()

    return save(entity)

def update(task: TaskUpdateForm, task_id: int) -> Task:
    with session() as db:
        entity = db.query(TaskEntity).get(task_id)
        assert entity, f'No task with id {task_id} exists'

        for key, value in task.dict(exclude_unset=True).items():
            setattr(entity, key, value)
        
        entity.updated_at = datetime.now()
        return save(entity)

def delete(task_id: int) -> Task:
    with session() as db:
        entity = db.query(TaskEntity).get(task_id)
        assert entity, f'No task with id {task_id} exists'

        db.delete(entity)
        db.commit()

        return Task.from_entity(entity)

def attach(task_id: int, company_user_id: int) -> int:
    with session() as db:
        entity = db.query(TaskEntity).get(task_id)
        assert entity, f'No task with id {task_id} exists'

        user_ids = [user_task.user_id for user_task in entity.user_tasks]
        assert company_user_id not in user_ids, f'User with id {company_user_id} is already attached to this task'

        entity.user_tasks.append(UserTask(user_id=company_user_id))
        if not db.is_modified(entity, include_collections=False):
            entity = db.merge(entity)

        db.add(entity)
        db.commit()

        return entity.id

def save(entity: TaskEntity) -> Task:
    with session() as db:
        'False -> detect only local-column based properties'
        if db.is_modified(entity, include_collections=False):
            entity = db.merge(entity)

        db.add(entity)
        db.commit()

        return Task.from_entity(entity)