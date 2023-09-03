from datetime import datetime
from models.subtask import Subtask, SubtaskEntity, SubtaskCreationForm, SubtaskUpdateForm
from database.database import session

def get_subtasks(task_id: int) -> list[Subtask]:
    with session() as db:
        entities = db.query(SubtaskEntity).filter(SubtaskEntity.task == task_id).all()
        return [Subtask.from_entity(entity) for entity in entities]

def create(subtask: SubtaskCreationForm, company_user_id: int) -> Subtask:
    entity = SubtaskEntity.from_model(subtask)
    entity.created_by = company_user_id
    entity.created_at = datetime.now()

    return save(entity)

def update(subtask_id: int, subtask: SubtaskUpdateForm) -> Subtask:
    with session() as db:
        entity = db.query(SubtaskEntity).get(subtask_id)
        assert entity, f'No subtask with id {subtask_id} exists'

        for key, value in subtask.dict(exclude_unset=True).items():
            setattr(entity, key, value)

        entity.updated_at = datetime.now()
        return save(entity)

def save(entity: SubtaskEntity) -> Subtask:
    with session() as db:
        'False -> detect only local-column based properties'
        if db.is_modified(entity, include_collections=False):
            entity = db.merge(entity)

        db.add(entity)
        db.commit()

        return Subtask.from_entity(entity)