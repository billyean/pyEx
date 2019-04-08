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


@pytest.fixture()
def a_tuple():
    """Return something more interesting."""
    return 1, 'foo', None, {'bar': 23}


def test_a_tuple(a_tuple):
    """Demo the a_tuple fixture."""
    assert a_tuple[3]['bar'] == 32


@pytest.fixture()
def some_other_data():
    """Raise an exception from fixture."""
    x = 43
    assert x == 42


def test_other_data(some_other_data):
    """Raise an exception from fixture."""
    pass


# Reminder of Task constructor interface
# Task(summary= None, owner= None, done= False, id= None)
# summary is required
# owner and done are optional
# id is set by database

@pytest.fixture()
def tasks_just_a_few():
    """All summaries and owners are unique."""
    return (
        Task('Write some code', 'Brian', True),
        Task("Code review Brian's code", 'Katie', False),
        Task('Fix what Brian did', 'Michelle', False)
    )


@pytest.fixture()
def tasks_mult_per_owner():
    """Several owners with several tasks each."""
    return (
        Task('Make a cookie', 'Raphael'),
        Task('Use an emoji', 'Raphael'),
        Task('Move to Berlin', 'Raphael'),

        Task('Create', 'Michelle'),
        Task('Inspire', 'Michelle'),
        Task('Encourage', 'Michelle'),

        Task('Do a handstand', 'Daniel'),
        Task('Write some books', 'Daniel'),
        Task('Eat ice cream', 'Daniel')
    )


@pytest.fixture()
def db_with_3_tasks(task_db, tasks_just_a_few):
    """Connect db with 3 tasks, all unique"""
    for task in tasks_just_a_few:
        tasks.add(task)


@pytest.fixture()
def db_with_mult_per_owner(task_db, tasks_mult_per_owner):
    """Connect db with 3 tasks, all unique"""
    for task in tasks_mult_per_owner:
        tasks.add(task)


def test_add_increases_count(db_with_3_tasks):
    """Test tasks.add() affect on tasks.count()"""
    # GIVEN a db with 3 tasks
    # WHEN another task is added
    tasks.add(Task('throw a party'))

    # THEN the count increases by 1
    assert tasks.count() == 4


@pytest.fixture(scope='function')
def func_scope():
    """A function scope fixture"""


@pytest.fixture(scope='module')
def mod_scope():
    """A module scope fixture"""


@pytest.fixture(scope='session')
def sess_scope():
    """A session scope fixture"""


@pytest.fixture(scope='class')
def class_scope():
    """A class scope fixture"""


def test_1(sess_scope, mod_scope, func_scope):
    """Test using session, module and function scope fixtures."""


def test_2(sess_scope, mod_scope, func_scope):
    """Demo is more fun with multiple tests."""


@pytest.mark.usefixtures('class_scope')
class TestSomething ():
    """Demo class scope fixtures"""

    def test_3(self):
        """Test using a class scope fixture."""

    def test_4(self):
        """Again , multiple tests are more fun."""
