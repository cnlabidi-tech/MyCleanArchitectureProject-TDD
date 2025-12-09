import pytest

from app.domain.use_cases.create_task import CreateTaskUseCase


def test_create_task_returns_task_with_given_data():
    use_case = CreateTaskUseCase()

    task = use_case.execute(title="Test task", description="Test description")

    assert task.title == "Test task"
    assert task.description == "Test description"
    assert task.is_completed is False
    assert task.id is not None


def test_create_task_raises_when_title_is_empty():
    use_case = CreateTaskUseCase()

    with pytest.raises(ValueError):
        use_case.execute(title="", description="Some description")


def test_create_task_raises_when_title_is_whitespace():
    use_case = CreateTaskUseCase()

    with pytest.raises(ValueError):
        use_case.execute(title="   ", description="Some description")
