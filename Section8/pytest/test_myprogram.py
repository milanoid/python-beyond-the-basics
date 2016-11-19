"""
run from command line:
    py.test

"""
import pytest

from Section8.pytest import myprogram


# import myprogram

class TestDoubleIt(object):
    def test_doubleit(self):
        assert myprogram.doubleit(10) == 20

    def test_doubleit_type(self):
        with pytest.raises(ValueError):
            assert myprogram.doubleit("astring")
