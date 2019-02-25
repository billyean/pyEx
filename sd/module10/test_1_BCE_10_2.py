import pytest


def test_eq():
    assert [1, 2, 3] == [1, 2, 3]
    assert (1, 2, 3) == (1, 2, 3)


def test_condition():
    assert [1, 2, 3] is not None


def test_less():
    assert [1, 2, 3] < [1, 2, 4]


@pytest.mark.parametrize('line1,line2',
                         [([3, 4, 5], [3, 4, 5]),
                          (1, 2 - 1),
                          ('hello', 'Hello'.lower())])
def test_eq_single(line1, line2):
    assert line1 == line2