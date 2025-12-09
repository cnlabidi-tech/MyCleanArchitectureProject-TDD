from typing import List

from app.domain.entities.task import Task


class ListTasksUseCase:
    def __init__(self, tasks: List[Task]) -> None:
        self._tasks = tasks

    def execute(self) -> List[Task]:
        return self._tasks
