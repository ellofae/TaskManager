from models.subtask import Subtask, SubtaskCreationForm, SubtaskUpdateForm
from repository.company_user_repository import CompanyUserRepository
from repository.subtask_repository import SubtaskRepository
from repository.task_repository import TaskRepository
from services.company_user_service import CompanyUserService
from services.subtask_service import SubtaskService
from services.task_service import TaskService


class SubtaskController:
    def __init__(self, ss: SubtaskService, ts: TaskService, cus: CompanyUserService):
        self.subtask_service = ss
        self.task_service = ts
        self.company_user_service = cus

    def create(self, subtask: SubtaskCreationForm, current_user_id: int) -> Subtask:
        task = self.task_service.get_task_by_id(subtask.task)

        user_to_check = self.company_user_service.check_weather_user_exists_wrapper(current_user_id, task.company_id)

        return self.subtask_service.create(subtask, user_to_check.id)

    def update(self, subtask_id: int, subtask: SubtaskUpdateForm, current_user_id: int) -> Subtask:
        assert subtask_id > 0, 'Subtask id must be greater than zero'
        subtask_to_update = self.subtask_service.get_subtask_entity_id(subtask_id)

        task = self.task_service.get_task_by_id(subtask_to_update.task)
        self.company_user_service.check_weather_user_exists_wrapper(current_user_id, task.company_id)

        return self.subtask_service.update(subtask_id, subtask)

    def delete(self, subtask_id: int, current_user_id: int) -> Subtask:
        subtask_to_update = self.subtask_service.get_subtask_entity_id(subtask_id)

        task = self.task_service.get_task_by_id(subtask_to_update.task)
        self.company_user_service.check_weather_user_exists_wrapper(current_user_id, task.company_id)

        return self.subtask_service.delete(subtask_id)

    def get_subtasks(self, task_id: int, current_user_id: int) -> list[Subtask]:
        task = self.task_service.get_task_by_id(task_id)
        self.company_user_service.check_weather_user_exists_wrapper(current_user_id, task.company_id)

        return self.subtask_service.get_subtasks(task_id)




def get_subtask_controller() -> SubtaskController:
    subtask_repository = SubtaskRepository()
    subtask_service = SubtaskService(subtask_repository)

    task_repository = TaskRepository()
    task_service = TaskService(task_repository)

    company_user_repository = CompanyUserRepository()
    company_user_service = CompanyUserService(company_user_repository)

    return SubtaskController(subtask_service, task_service, company_user_service)