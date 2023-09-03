import repository.task as repo
import services.company_user as company_user_service
import services.subtask as subtask_service
from database.database import session
from models.task import Task, TaskCreationForm, TaskEntity, TaskUpdateForm
from models.subtask import Subtask

def get_subtasks(task_id: int, current_user_id: int) -> list[Subtask]:
    assert task_id > 0, 'Task id must be graeter than zero'

    task = repo.get_task_by_id(task_id)
    return subtask_service.get_subtasks(task_id, current_user_id, task.company)

def get_all_tasks(company_user_id: int) -> list[Task]:
    with session() as db:
        entities = db.query(TaskEntity).filter(TaskEntity.created_by == company_user_id).order_by(TaskEntity.id.desc()).all()
        return [Task.from_entity(entity) for entity in entities]

def get_task_by_id(task_id: int, current_user_id: int) -> Task:
    assert task_id > 0, 'Task id must be greater than zero'
    task = repo.get_task_by_id(task_id)

    company_user = company_user_service.check_weather_user_exists(current_user_id, task.company)
    assert company_user, f'Current user is not attached to the company with id {task.company}'

    return task

def create(task: TaskCreationForm, current_user_id: int) -> Task:
    company_user = company_user_service.check_weather_user_exists(current_user_id, task.company)
    assert company_user, f'User is not attached to company with id {task.company}'
    return repo.create(task, company_user.id)

def update(task: TaskUpdateForm, task_id: int, current_user_id: int) -> Task:
    assert task_id > 0, 'Task id must be greater than zero'

    task_by_id = repo.get_task_by_id(task_id)
    company_user = company_user_service.check_weather_user_exists(current_user_id, task_by_id.company)
    assert company_user, f'User is not attached to company with id {task_by_id.company}'

    return repo.update(task, task_id)

def delete(task_id: int, current_user_id: int) -> Task:
    assert task_id > 0, 'Task id must be greater than zero'

    task_by_id = repo.get_task_by_id(task_id)
    company_user = company_user_service.check_weather_user_exists(current_user_id, task_by_id.company)
    assert company_user, f'User is not attached to company with id {task_by_id.company}'

    return repo.delete(task_id)