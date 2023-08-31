from fastapi import APIRouter
from models.task import Task

task_router = APIRouter()

@task_router.post('/', status_code=201, tags=['tasks'])
async def create(task: Task) -> Task:
    pass