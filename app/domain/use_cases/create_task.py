from app.domain.entities.task import Task


class CreateTaskUseCase:
    def __init__(self) -> None:
        self._next_id = 1

    def execute(self, title: str, description: str) -> Task:
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")

        task = Task(id=self._next_id, title=title, description=description, is_completed=False)
        self._next_id += 1
        return task
