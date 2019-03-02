import pytest


def divide(numerator, denominator):
    return numerator / denominator


def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
