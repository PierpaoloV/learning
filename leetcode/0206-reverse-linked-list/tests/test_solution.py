import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from solution import reverse_list, ListNode


def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def to_linked(vals):
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def test_basic():
    assert to_list(reverse_list(to_linked([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]

def test_two_nodes():
    assert to_list(reverse_list(to_linked([1, 2]))) == [2, 1]

def test_empty():
    assert reverse_list(None) is None

def test_single():
    assert to_list(reverse_list(to_linked([1]))) == [1]
