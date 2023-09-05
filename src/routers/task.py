from typing import Annotated

import services.task as service
from common.current_user_data import get_current_user_id
from fastapi import APIRouter, Depends
from models.subtask import Subtask
from models.task import Task, TaskCreationForm, TaskUpdateForm
from models.user import UserAttachForm

task_router = APIRouter()

@task_router.get('/{task_id}/subtasks', response_model=list[Subtask], response_model_exclude_none=True, status_code=200, tags=['tasks'])
async def get_subtasks(task_id: int, current_user_id: Annotated[int, Depends(get_current_user_id)]) -> list[Subtask]:
    return service.get_subtasks(task_id, current_user_id)

@task_router.get('/{task_id}', response_model=Task, response_model_exclude_none=True, status_code=200, tags=['tasks'])
async def get_task_by_id(task_id: int, current_user_id: Annotated[int, Depends(get_current_user_id)]) -> Task:
    return service.get_task_by_id(task_id, current_user_id)

@task_router.post('/', response_model=Task, response_model_exclude_none=True, status_code=201, tags=['tasks'])
async def create(task: TaskCreationForm, current_user_id: Annotated[int, Depends(get_current_user_id)]) -> Task:
    return service.create(task, current_user_id)

@task_router.post('/{task_id}/attach_user', status_code=201, tags=['tasks'])
async def attach(task_id: int, user_attach: UserAttachForm, current_user_id: Annotated[int, Depends(get_current_user_id)]):
    company_user_id = service.attach(task_id, user_attach, current_user_id)
    return {'message': 'user attached', 'company user id': company_user_id, 'task id': task_id}

@task_router.patch('/{task_id}', response_model=Task, response_model_exclude_none=True, status_code=200, tags=['tasks'])
async def update(task: TaskUpdateForm, task_id: int, current_user_id: Annotated[int, Depends(get_current_user_id)]) -> Task:
    return service.update(task, task_id, current_user_id)

@task_router.delete('/{task_id}', status_code=200, tags=['tasks'])
async def delete(task_id: int, current_user_id: Annotated[int, Depends(get_current_user_id)]):
    task_deleted = service.delete(task_id, current_user_id)
    return {'message': 'task deleted', 'task_id': task_deleted.id}