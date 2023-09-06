from datetime import datetime
from models.task import Task, TaskEntity, TaskCreationForm
from repository.task_repository import TaskRepository


class TaskService:
    def __init__(self, repo: TaskRepository):
        self.repo = repo

    def create(self, task: TaskCreationForm, company_user_id: int) -> Task:
        entity = TaskEntity.from_model(task)
        entity.created_by = company_user_id
        entity.created_at = datetime.now()

        return self.repo.save(entity)


    def get_all_tasks(self, company_id: int) -> list[Task]:
        assert company_id > 0, 'Company id must be greater than zero'
        return self.repo.get_all_tasks(company_id)