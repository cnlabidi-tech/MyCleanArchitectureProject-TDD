from typing import Optional

from app.domain.entities.task import Task


class CreateTaskUseCase:
    def __init__(self) -> None:
        self._next_id = 1

    def execute(self, title: str, description: str) -> Task:
        task = Task(id=self._next_id, title=title, description=description, is_completed=False)
        self._next_id += 1
        return task
