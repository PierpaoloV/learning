import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from solution import group_anagrams


def _normalize(result):
    return sorted([sorted(g) for g in result])

def test_basic():
    result = group_anagrams(["eat","tea","tan","ate","nat","bat"])
    assert _normalize(result) == _normalize([["bat"],["nat","tan"],["ate","eat","tea"]])

def test_single_empty_string():
    assert group_anagrams([""]) == [[""]]

def test_single_char():
    assert group_anagrams(["a"]) == [["a"]]

def test_all_anagrams():
    result = group_anagrams(["abc", "bca", "cab"])
    assert _normalize(result) == [["abc", "bca", "cab"]]

def test_no_anagrams():
    result = group_anagrams(["abc", "def", "ghi"])
    assert _normalize(result) == _normalize([["abc"], ["def"], ["ghi"]])
