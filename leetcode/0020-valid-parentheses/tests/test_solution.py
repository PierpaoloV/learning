import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from solution import is_valid


def test_simple_pair():
    assert is_valid("()") is True

def test_multiple_types():
    assert is_valid("()[]{}") is True

def test_wrong_close():
    assert is_valid("(]") is False

def test_wrong_order():
    assert is_valid("([)]") is False

def test_nested():
    assert is_valid("{[]}") is True

def test_single_open():
    assert is_valid("(") is False

def test_single_close():
    assert is_valid(")") is False
