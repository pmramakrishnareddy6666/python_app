from src.math_opt import add, sub, mul, div

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_sub():
    assert sub(5, 3) == 2
    assert sub(4, 8) == -4
    assert sub(4, 4) == 0

def test_mul():
    assert mul(10, 2) == 20
    assert mul(2, 4) == 8

def test_div():
    assert div(4, 2) == 2