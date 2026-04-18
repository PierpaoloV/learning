import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from solution import two_sum


def test_basic():
    assert sorted(two_sum([2, 7, 11, 15], 9)) == [0, 1]

def test_duplicate_values():
    assert sorted(two_sum([3, 2, 4], 6)) == [1, 2]

def test_same_element_not_reused():
    assert sorted(two_sum([3, 3], 6)) == [0, 1]

def test_negative_numbers():
    assert sorted(two_sum([-1, -2, -3, -4, -5], -8)) == [2, 4]
