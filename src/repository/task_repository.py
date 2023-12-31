from datetime import datetime

from database.database import session
from models.company import CompanyEntity
from models.task import Task, TaskEntity, TaskUpdateForm
from models.user_task import UserTask


class TaskRepository:
    # Command module
    def save(self, entity: TaskEntity) -> Task:
        with session() as db:
            'False -> detect only local-column based properties'
            if db.is_modified(entity, include_collections=False):
                entity = db.merge(entity)

            db.add(entity)
            db.commit()

            return Task.from_entity(entity)

    def update(self, entity_to_update: TaskEntity, task: TaskUpdateForm) -> Task:
        with session() as db:
            db.merge(entity_to_update)

            for key, value in task.dict(exclude_unset=True).items():
                setattr(entity_to_update, key, value)

            entity_to_update.updated_at = datetime.now()
            return self.save(entity_to_update)

    def delete(self, entity: TaskEntity) -> Task:
        with session() as db:
            db.delete(entity)
            db.commit()

            return Task.from_entity(entity)

    def attach(self, entity: TaskEntity, company_user_id: int) -> int:
        with session() as db:
            entity = db.merge(entity)

            user_ids = [user_task.user_id for user_task in entity.user_tasks]
            assert company_user_id not in user_ids, f'User with id {company_user_id} is already attached to this task'

            entity.user_tasks.append(UserTask(user_id=company_user_id))
            if not db.is_modified(entity, include_collections=False):
                entity = db.merge(entity)

            db.add(entity)
            db.commit()

            return entity.id

    # Querying module
    def get_all_tasks(self, company_id: int) -> list[Task]:
        with session() as db:
            entities = db.query(TaskEntity).join(TaskEntity.company).filter(CompanyEntity.id == company_id).order_by(TaskEntity.id.desc()).all()
            return [Task.from_entity(entity) for entity in entities]

    def get_task_by_id(self, task_id: int) -> Task:
        with session() as db:
            entity = db.query(TaskEntity).get(task_id)
            assert entity, f'No task with id {task_id} exists'

            return Task.from_entity(entity)

    def get_task_entity_by_id(self, task_id: int) -> TaskEntity:
        with session() as db:
            entity = db.query(TaskEntity).get(task_id)
            assert entity, f'No task with id {task_id} exists'

            return entity