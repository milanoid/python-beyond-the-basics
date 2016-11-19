from Section8.pytest import myprogram


def test_doubleit():
    assert myprogram.doubleit(10) == 20
