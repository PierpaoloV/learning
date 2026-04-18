import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from solution import length_of_longest_substring


def test_basic():
    assert length_of_longest_substring("abcabcbb") == 3

def test_all_same():
    assert length_of_longest_substring("bbbbb") == 1

def test_mixed():
    assert length_of_longest_substring("pwwkew") == 3

def test_empty():
    assert length_of_longest_substring("") == 0

def test_single():
    assert length_of_longest_substring("a") == 1

def test_all_unique():
    assert length_of_longest_substring("abcdef") == 6
