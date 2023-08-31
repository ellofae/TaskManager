from datetime import datetime
from database.database import session
from models.task import Task, TaskEntity, TaskCreationForm, TaskUpdateForm

def get_task_by_id(task_id: int, current_user_id: int) -> Task:
    with session() as db:
        entity = db.query(TaskEntity).filter(TaskEntity.user_id == current_user_id, TaskEntity.id == task_id).first()
        assert entity, f'No task with id {task_id} exists for current user'

        return Task.from_entity(entity)

def create(task: TaskCreationForm, current_user_id: int) -> Task:
    entity = TaskEntity.from_model(task)
    entity.user_id = current_user_id
    entity.created_at = datetime.now()

    return save(entity)

def update(task: TaskUpdateForm, task_id: int, current_user_id: int) -> Task:
    with session() as db:
        entity = db.query(TaskEntity).filter(TaskEntity.id == task_id, TaskEntity.user_id == current_user_id).first()
        assert entity, f'No task with id {task_id} exists for current user'

        for key, value in task.dict(exclude_unset=True).items():
            setattr(entity, key, value)
        
        entity.updated_at = datetime.now()
        return save(entity)

def delete(task_id: int, current_user_id: int) -> Task:
    with session() as db:
        entity = db.query(TaskEntity).filter(TaskEntity.id == task_id, TaskEntity.user_id == current_user_id).first()
        assert entity, f'No task with id {task_id} exists for current user'

        db.delete(entity)
        db.commit()

        return Task.from_entity(entity)

def save(entity: TaskEntity) -> Task:
    with session() as db:
        'False -> detect only local-column based properties'
        if db.is_modified(entity, include_collections=False):
            entity = db.merge(entity)

        db.add(entity)
        db.commit()

        return Task.from_entity(entity)