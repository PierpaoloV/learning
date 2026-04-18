import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from solution import max_profit


def test_basic():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5

def test_no_profit():
    assert max_profit([7, 6, 4, 3, 1]) == 0

def test_single_day():
    assert max_profit([5]) == 0

def test_two_days_profit():
    assert max_profit([1, 2]) == 1

def test_buy_low_sell_high():
    assert max_profit([3, 1, 4, 1, 5, 9, 2, 6]) == 8
