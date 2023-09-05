import repository.task as repo
import services.company_user as company_user_service
import services.subtask as subtask_service
from database.database import session
from models.subtask import Subtask
from models.task import Task, TaskCreationForm, TaskEntity, TaskUpdateForm
from models.user import UserAttachForm


def get_subtasks(task_id: int, current_user_id: int) -> list[Subtask]:
    assert task_id > 0, 'Task id must be graeter than zero'
    task = repo.get_task_by_id(task_id)
    return subtask_service.get_subtasks(task_id, current_user_id, task.company_id)

def get_all_tasks(company_user_id: int) -> list[Task]:
    with session() as db:
        entities = db.query(TaskEntity).filter(TaskEntity.created_by == company_user_id).order_by(TaskEntity.id.desc()).all()
        return [Task.from_entity(entity) for entity in entities]

def get_task_by_id(task_id: int, current_user_id: int) -> Task:
    assert task_id > 0, 'Task id must be greater than zero'
    task = repo.get_task_by_id(task_id)

    company_user_service.check_weather_user_exists(current_user_id, task.company_id)
    return task

def create(task: TaskCreationForm, current_user_id: int) -> Task:
    company_user = company_user_service.check_weather_user_exists(current_user_id, task.company_id)
    return repo.create(task, company_user.id)

def attach(task_id: int, user_attach: UserAttachForm, current_user_id: int) -> int:
    task_by_id = repo.get_task_by_id(task_id)
    company_user_service.check_weather_user_exists(current_user_id, task_by_id.company_id)

    company_user = company_user_service.get_company_user_by_id(user_attach.company_user_id, current_user_id)
    repo.attach(task_id, user_attach.company_user_id)

    return company_user.id




def update(task: TaskUpdateForm, task_id: int, current_user_id: int) -> Task:
    assert task_id > 0, 'Task id must be greater than zero'

    task_by_id = repo.get_task_by_id(task_id)
    company_user_service.check_weather_user_exists(current_user_id, task_by_id.company_id)
    return repo.update(task, task_id)

def delete(task_id: int, current_user_id: int) -> Task:
    assert task_id > 0, 'Task id must be greater than zero'

    task_by_id = repo.get_task_by_id(task_id)
    company_user_service.check_weather_user_exists(current_user_id, task_by_id.company_id)
    return repo.delete(task_id)