from models.task import Task, TaskCreationForm, TaskUpdateForm
from models.user import UserAttachForm
from repository.task_repository import TaskRepository
from services.task_service import TaskService

from repository.company_user_repository import CompanyUserRepository
from repository.company_repository import CompanyRepository
from services.company_user_service import CompanyUserService
from services.company_service import CompanyService


class TaskController:
    def __init__(self, ts: TaskService, cus: CompanyUserService, cs: CompanyService):
        self.task_service = ts
        self.company_user_service = cus
        self.company_service = cs

    def create(self, task: TaskCreationForm, current_user_id: int) -> Task:
        self.company_service.get_company_by_id(task.company_id)

        company_user = self.company_user_service.check_weather_user_exists(current_user_id, task.company_id)
        assert company_user, f'User with id {current_user_id} is not registered for company with id {task.company_id}'

        return self.task_service.create(task, company_user.id)

    def update(self, task_update_form: TaskUpdateForm, task_id: int, current_user_id: int) -> Task:
        task = self.task_service.get_task_by_id(task_id)

        user_to_check = self.company_user_service.check_weather_user_exists(current_user_id, task.company_id)
        assert user_to_check, f'User with id {current_user_id} is not registered for company with id {task.company_id}'

        return self.task_service.update(task_update_form, task_id)

    def delete(self, task_id: int, current_user_id: int) -> Task:
        task = self.task_service.get_task_by_id(task_id)

        user_to_check = self.company_user_service.check_weather_user_exists(current_user_id, task.company_id)
        assert user_to_check, f'User with id {current_user_id} is not registered for company with id {task.company_id}'

        return self.task_service.delete(task_id)

    def attach(self, task_id: int, user_attach: UserAttachForm, current_user_id: int) -> int:
        task = self.task_service.get_task_by_id(task_id)

        user_to_check = self.company_user_service.check_weather_user_exists(current_user_id, task.company_id)
        assert user_to_check, f'User with id {current_user_id} is not registered for company with id {task.company_id}'

        'Checking if company user with such id exists'
        company_user = self.company_user_service.get_company_user_by_id(user_attach.company_user_id, current_user_id)
        self.task_service.attach(task_id, company_user.id)

        return company_user.id

    def get_task_by_id(self, task_id: int, current_user_id: int) -> Task:
        task = self.task_service.get_task_by_id(task_id)

        user_to_check = self.company_user_service.check_weather_user_exists(current_user_id, task.company_id)
        assert user_to_check, f'User with id {current_user_id} is not registered for company with id {task.company_id}'

        return task

    def get_all_tasks(self, company_id: int, user_id: int) -> list[Task]:
        user_to_check = self.company_user_service.check_weather_user_exists(user_id, company_id)
        assert user_to_check, f'User with id {user_id} is not registered for company with id {company_id}'

        return self.task_service.get_all_tasks(company_id)

def get_task_controller() -> TaskController:
    task_repository = TaskRepository()
    task_service = TaskService(task_repository)

    company_user_repository = CompanyUserRepository()
    company_user_service = CompanyUserService(company_user_repository)

    company_repository = CompanyRepository()
    company_service = CompanyService(company_repository)

    return TaskController(task_service, company_user_service, company_service)