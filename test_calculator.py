from calculator import *

def test_add():
    assert add(2,3) == 5

def test_sub():
    assert substract(5,2) == 3
def test_mul():
    assert mul(2,3) == 6
def test_div():
    assert div(6,2) == 3
def test_mod():
    assert mod(3,4) == 3
