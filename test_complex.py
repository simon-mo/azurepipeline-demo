import pytest
import itertools

@pytest.mark.parametrize(
    "arg1, arg2",
    [(i,j) for i, j in itertools.product(list(range(50)),repeat=2)])
def test_param(arg1, arg2):
    if arg1 + arg2 == 64:
        assert False
    assert True
