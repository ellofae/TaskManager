from datetime import datetime
from models.task import Task, TaskEntity, TaskCreationForm, TaskUpdateForm
from models.user import UserAttachForm
from repository.task_repository import TaskRepository


class TaskService:
    def __init__(self, repo: TaskRepository):
        self.repo = repo

    def create(self, task: TaskCreationForm, company_user_id: int) -> Task:
        entity = TaskEntity.from_model(task)
        entity.created_by = company_user_id
        entity.created_at = datetime.now()

        return self.repo.save(entity)

    def update(self, task: TaskUpdateForm, task_id: int) -> Task:
        assert task_id > 0, 'Task id must be greater than zero'
        task_entity_to_update = self.repo.get_task_entity_by_id(task_id)

        return self.repo.update(task_entity_to_update, task)

    def delete(self, task_id: int) -> Task:
        assert task_id > 0, 'Task id must be greater than zero'
        task_entity_to_delete = self.repo.get_task_entity_by_id(task_id)

        return self.repo.delete(task_entity_to_delete)

    def attach(self, task_id: int, company_user_id: int) -> int:
        assert task_id > 0, 'Task id must be greater than zero'
        task_entity = self.repo.get_task_entity_by_id(task_id)

        return self.repo.attach(task_entity, company_user_id)

    def get_task_by_id(self, task_id: int) -> Task:
        assert task_id > 0, 'Task id must be greater than zero'
        task = self.repo.get_task_by_id(task_id)

        return task


def get_all_tasks(self, company_id: int) -> list[Task]:
        assert company_id > 0, 'Company id must be greater than zero'
        return self.repo.get_all_tasks(company_id)