import pytest
import itertools

@pytest.mark.parametrize(
    "arg1, arg2",
    [(i,j) for i, j in itertools.product(list(range(3)),repeat=2)])
def test_param(arg1, arg2):
    if arg1 + arg2 == 2:
        assert False
    assert True

@pytest.mark.skip(reason="no way of currently testing this")
def test_skil():
    pass
