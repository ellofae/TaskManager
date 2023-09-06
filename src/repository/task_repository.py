from models.task import Task, TaskEntity
from models.company import CompanyEntity
from database.database import session

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

    # Querying module
    def get_all_tasks(self, company_id: int) -> list[Task]:
        with session() as db:
            entities = db.query(TaskEntity).join(TaskEntity.company).filter(CompanyEntity.id == company_id).order_by(TaskEntity.id.desc()).all()
            return [Task.from_entity(entity) for entity in entities]