from datetime import datetime
from models.subtask import Subtask, SubtaskEntity, SubtaskUpdateForm
from database.database import session

class SubtaskRepository:
    # Command module
    def save(self, entity: SubtaskEntity) -> Subtask:
        with session() as db:
            'False -> detect only local-column based properties'
            if db.is_modified(entity, include_collections=False):
                entity = db.merge(entity)

            db.add(entity)
            db.commit()

            return Subtask.from_entity(entity)

    def delete(self, entity: SubtaskEntity) -> Subtask:
        with session() as db:
            db.delete(entity)
            db.commit()

            return Subtask.from_entity(entity)


    # Querying module
    def get_subtask_entity_id(self, subtask_id: int) -> SubtaskEntity:
        with session() as db:
            entity = db.query(SubtaskEntity).get(subtask_id)
            assert entity, f'No subtask with id {subtask_id} exists'

            return entity

    def get_subtasks(self, task_id: int) -> list[Subtask]:
        with session() as db:
            entities = db.query(SubtaskEntity).filter(SubtaskEntity.task == task_id).all()
            return [Subtask.from_entity(entity) for entity in entities]