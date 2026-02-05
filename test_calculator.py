from calculator import add,substract

def test_add():
    assert add(2,3) == 5
    assert add(5,3) == 9

def test_sub():
    assert substract(5,2) == 3
