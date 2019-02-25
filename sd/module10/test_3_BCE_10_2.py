import pytest


@pytest.fixture()
def data():
    return [1, 2, 3]


def test_data_len(data):
    assert len(data) == 3


def test_data_ordered(data):
    assert data == sorted(data)

