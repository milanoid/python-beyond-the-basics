"""
run from command line:
    py.test

"""
import pytest

from Section8.pytest import myprogram


# import myprogram


def test_doubleit():
    assert myprogram.doubleit(10) == 20


def test_doubleit_type():
    with pytest.raises(ValueError):
        assert myprogram.doubleit("astring")
