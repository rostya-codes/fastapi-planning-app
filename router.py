from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STaskAdd

router = APIRouter(
    prefix='/tasks',
    tags=['Tasks']  # title
)


@router.post('')
async def add_task(
        task: Annotated[STaskAdd, Depends()]
):
    task_id = await TaskRepository.add_one(task)
    return {'ok': True, 'task_id': task_id}


@router.get('')
async def get_tasks():
    tasks = await TaskRepository.find_all()
    return {'data': tasks}
