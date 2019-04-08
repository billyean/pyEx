import pytest
import tasks
from tasks import Task


@pytest.fixture()
def some_data():
    """Return answer to ultimate questions."""
    return 42


def test_some_data(some_data):
    """Use fixture return value in a test."""
    assert some_data == 42


@pytest.fixture()
def task_db(tmpdir):
    """Connect to db before tests, disconnect after."""
    # Setup: start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield  # this is where the testing happens
    tasks.stop_tasks_db()


def test_add_returns_valid_id(task_db):
    """tasks.add(<valid task>) should return an integer."""
    # GIVEN an initialized tasks db
    # WHEN a new task is added
    # THEN returned ask_id is of type int
    new_task = Task('do something')
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)
