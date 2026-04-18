import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from solution import is_palindrome


def test_classic():
    assert is_palindrome("A man, a plan, a canal: Panama") is True

def test_not_palindrome():
    assert is_palindrome("race a car") is False

def test_empty_after_strip():
    assert is_palindrome(" ") is True

def test_numbers():
    assert is_palindrome("0P") is False

def test_single_char():
    assert is_palindrome("a") is True
