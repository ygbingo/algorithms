from cut_rod import memoized_cut_rod, bottom_up_cut_rod


p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

def test_cut_rod():
    assert memoized_cut_rod(p, 5) == 13
    assert memoized_cut_rod(p, 10) == 30
    assert memoized_cut_rod(p, 0) == 0
    assert bottom_up_cut_rod(p, 5)[0][-1] == 13