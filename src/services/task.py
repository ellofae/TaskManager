import repository.task as repo
from database.database import session
from models.task import Task, TaskCreationForm, TaskEntity, TaskUpdateForm

def get_all_records(current_user_id: int) -> list[Task]:
    with session() as db:
        entities = db.query(TaskEntity).filter(TaskEntity.user_id == current_user_id).order_by(TaskEntity.id.desc()).all()
        return [Task.from_entity(entity) for entity in entities]

def get_task_by_id(task_id: int, current_user_id: int) -> Task:
    assert task_id > 0, 'Task id must be greater than zero'
    return repo.get_task_by_id(task_id, current_user_id)

def create(task: TaskCreationForm, current_user_id: int) -> Task:
    return repo.create(task, current_user_id)

def update(task: TaskUpdateForm, task_id: int, current_user_id: int) -> Task:
    assert task_id > 0, 'Task id must be greater than zero'
    return repo.update(task, task_id, current_user_id)

def delete(task_id: int, current_user_id: int) -> Task:
    assert task_id > 0, 'Task id must be greater than zero'
    return repo.delete(task_id, current_user_id)