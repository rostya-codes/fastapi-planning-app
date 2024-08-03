from sqlalchemy import select

from database import TaskOrm, new_session
from schemas import STaskAdd


class TaskRepository:

    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session as session:
            task_dict = data.model_dump()  # Преобразование в словарь

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(self):
        async with new_session as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            return task_models
