from app.domain.entities.task import Task
from app.domain.use_cases.list_tasks import ListTasksUseCase


def test_list_tasks_returns_all_existing_tasks():
    existing_tasks = [
        Task(id=1, title="Task 1", description="Desc 1", is_completed=False),
        Task(id=2, title="Task 2", description="Desc 2", is_completed=True),
    ]

    use_case = ListTasksUseCase(tasks=existing_tasks)

    result = use_case.execute()

    assert result == existing_tasks
