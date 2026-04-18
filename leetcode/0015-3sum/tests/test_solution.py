import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from solution import three_sum


def _normalize(result):
    return sorted([sorted(t) for t in result])

def test_basic():
    assert _normalize(three_sum([-1, 0, 1, 2, -1, -4])) == [[-1, -1, 2], [-1, 0, 1]]

def test_no_result():
    assert three_sum([0, 1, 1]) == []

def test_all_zeros():
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]

def test_no_duplicates_in_output():
    result = three_sum([-2, 0, 0, 2, 2])
    assert _normalize(result) == [[-2, 0, 2]]
