from datetime import datetime

from models.subtask import Subtask, SubtaskCreationForm, SubtaskEntity, SubtaskUpdateForm
from repository.subtask_repository import SubtaskRepository


class SubtaskService:
    def __init__(self, repo: SubtaskRepository):
        self.repo = repo

    def create(self, subtask: SubtaskCreationForm, company_user_id: int) -> Subtask:
        entity = SubtaskEntity.from_model(subtask)
        entity.created_by = company_user_id
        entity.created_at = datetime.now()

        return self.repo.save(entity)

    def update(self, subtask_id: int, subtask: SubtaskUpdateForm) -> Subtask:
        assert subtask_id > 0, 'Subtask id must be greater than zero'
        subtask_entity = self.repo.get_subtask_entity_id(subtask_id)

        for key, value in subtask.dict(exclude_unset=True).items():
            setattr(subtask_entity, key, value)

        subtask_entity.updated_at = datetime.now()

        return self.repo.save(subtask_entity)

    def delete(self, subtask_id: int) -> Subtask:
        assert subtask_id > 0, 'Subtask id must be greater than zero'

        subtask_entity = self.repo.get_subtask_entity_id(subtask_id)
        return self.repo.delete(subtask_entity)

    def get_subtask_entity_id(self, subtask_id: int) -> SubtaskEntity:
        return self.repo.get_subtask_entity_id(subtask_id)

    def get_subtasks(self, task_id: int) -> list[Subtask]:
        return self.repo.get_subtasks(task_id)