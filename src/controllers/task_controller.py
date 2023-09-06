from models.task import Task
from repository.task_repository import TaskRepository
from services.task_service import TaskService

from repository.company_user_repository import CompanyUserRepository
from services.company_user_service import CompanyUserService


class TaskController:
    def __init__(self, ts: TaskService, cus: CompanyUserService):
        self.task_service = ts
        self.company_user_service = cus

    def get_all_tasks(self, company_id: int, user_id: int) -> list[Task]:
        user_to_check = self.company_user_service.check_weather_user_exists(user_id, company_id)
        assert user_to_check, f'User with id {user_id} is not registered for company with id {company_id}'

        return self.task_service.get_all_tasks(company_id)

def get_task_controller() -> TaskController:
    task_repository = TaskRepository()
    task_service = TaskService(task_repository)

    company_user_repository = CompanyUserRepository()
    company_user_service = CompanyUserService(company_user_repository)

    return TaskController(task_service, company_user_service)