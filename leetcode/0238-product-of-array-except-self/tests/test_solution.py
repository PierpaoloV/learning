import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from solution import product_except_self


def test_basic():
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]

def test_with_zero():
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]

def test_two_elements():
    assert product_except_self([3, 4]) == [4, 3]

def test_with_negatives():
    assert product_except_self([-1, -2, -3]) == [6, 3, 2]

def test_with_one():
    assert product_except_self([1, 1, 1, 1]) == [1, 1, 1, 1]
