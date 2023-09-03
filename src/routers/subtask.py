import services.subtask as service
from fastapi import APIRouter, Depends
from typing import Annotated
from models.subtask import SubtaskCreationForm, Subtask
from common.current_user_data import get_current_user_id

subtask_router = APIRouter()

@subtask_router.post('/', response_model=Subtask, response_model_exclude_unset=True, status_code=201, tags=['subtasks'])
async def create(subtask: SubtaskCreationForm, current_user_id: Annotated[int, Depends(get_current_user_id)]) -> Subtask:
    return service.create(subtask, current_user_id)
