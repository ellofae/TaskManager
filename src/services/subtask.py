import repository.subtask as repo
import services.company_user as company_user_service
import services.task as task_service
from models.subtask import Subtask, SubtaskCreationForm, SubtaskUpdateForm

def get_subtasks(task_id: int, current_user_id: int, company_id: int) -> list[Subtask]:
    company_user_service.check_weather_user_exists(current_user_id, company_id)
    return repo.get_subtasks(task_id)

def create(subtask: SubtaskCreationForm, current_user_id: int) -> Subtask:
    task = task_service.get_task_by_id(subtask.task, current_user_id)
    company_user = company_user_service.check_weather_user_exists(current_user_id, task.company)
    return repo.create(subtask, company_user.id)

def update(subtask_id: int, subtask: SubtaskUpdateForm, current_user_id: int) -> Subtask:
    assert subtask_id > 0, 'Subtask id must be greater than zero'
    task = task_service.get_task_by_id(subtask_id, current_user_id)

    company_user_service.check_weather_user_exists(current_user_id, task.company)
    return repo.update(subtask_id, subtask)

def delete(subtask_id: int, current_user_id: int) -> Subtask:
    assert subtask_id > 0, 'Subtask id must be greater than zero'
    task = task_service.get_task_by_id(subtask_id, current_user_id)

    company_user_service.check_weather_user_exists(current_user_id, task.company)
    return repo.delete(subtask_id)