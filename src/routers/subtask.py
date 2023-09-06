from typing import Annotated

import services.subtask as service
from common.current_user_data import get_current_user_id
from fastapi import APIRouter, Depends
from models.subtask import SubtaskCreationForm, Subtask, SubtaskUpdateForm

from controllers.subtask_controller import get_subtask_controller

subtask_router = APIRouter()
@subtask_router.post('/', response_model=Subtask, response_model_exclude_none=True, status_code=201, tags=['subtasks'])
async def create(subtask: SubtaskCreationForm, current_user_id: Annotated[int, Depends(get_current_user_id)]) -> Subtask:
    subtask_controller = get_subtask_controller()
    return subtask_controller.create(subtask, current_user_id)

@subtask_router.patch('/{subtask_id}', response_model=Subtask, response_model_exclude_none=True, status_code=200, tags=['subtasks'])
async def update(subtask_id: int, subtask: SubtaskUpdateForm, current_user_id: Annotated[int, Depends(get_current_user_id)]) -> Subtask:
    subtask_controller = get_subtask_controller()
    return subtask_controller.update(subtask_id, subtask, current_user_id)

@subtask_router.delete('/{subtask_id}', response_model=Subtask, response_model_exclude_none=True, status_code=200, tags=['subtasks'])
async def delete(subtask_id: int, current_user_id: Annotated[int, Depends(get_current_user_id)]) -> Subtask:
    subtask_controller = get_subtask_controller()
    subtask_deleted = subtask_controller.delete(subtask_id, current_user_id)
    return {'message': 'subtask deleted', 'deleted subtask id': subtask_deleted.id}