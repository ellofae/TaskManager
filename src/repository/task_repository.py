from models.task import Task, TaskEntity
from models.company import CompanyEntity
from database.database import session

class TaskRepository:
    # Command module

    # Querying module
    def get_all_tasks(self, company_id: int) -> list[Task]:
        with session() as db:
            entities = db.query(TaskEntity).join(TaskEntity.company).filter(CompanyEntity.id == company_id).order_by(TaskEntity.id.desc()).all()
            return [Task.from_entity(entity) for entity in entities]