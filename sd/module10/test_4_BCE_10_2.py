import pytest


@pytest.mark.xfail()
def test_supposed_failure():
    with open('in.txt', 'rt') as input:
        assert input is not None


def test():
    pass


@pytest.mark.skip()
def test_skip():
    assert test(3, 2, 1) == (1, 2, 3)


test_func_flag = None


def test_func(*var):
    pass


@pytest.mark.skipif(test_func_flag is None, reason="won't module11 test_func since it is not ready")
def test_skipif():
    assert test_func(3, 2, 1) == (1, 2, 3)
