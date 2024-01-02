from cut_rod import memoized_cut_rod, bottom_up_cut_rod
from longest_valid_parentheses import longest_valid_parentheses


p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

def test_cut_rod():
    assert memoized_cut_rod(p, 5) == 13
    assert memoized_cut_rod(p, 10) == 30
    assert memoized_cut_rod(p, 0) == 0
    assert bottom_up_cut_rod(p, 5)[0][-1] == 13

def test_lvp():
    s = "(()))())("
    assert longest_valid_parentheses(s) == 4


from getMaxRepetitions_466 import get_max_repetitions


def test_466():
    s1, n1, s2, n2 = "acb", 4, "ab", 2
    assert get_max_repetitions(s1, n1, s2, n2) == 2
    s1, n1, s2, n2 = "acb", 1, "acb", 1
    assert get_max_repetitions(s1, n1, s2, n2) == 1