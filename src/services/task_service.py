from models.task import Task
from repository.task_repository import TaskRepository


class TaskService:
    def __init__(self, repo: TaskRepository):
        self.repo = repo

    def get_all_tasks(self, company_id: int) -> list[Task]:
        assert company_id > 0, 'Company id must be greater than zero'
        return self.repo.get_all_tasks(company_id)