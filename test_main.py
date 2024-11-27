from main import add, subtract, multiply

def test_add():
    assert add(3, 5) == 8
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5
    assert subtract(7, 7) == 0

def test_multiply():
    assert multiply(6, 7) == 42
    assert multiply(0, 5) == 0
    assert multiply(-3, 3) == -9
