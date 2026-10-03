from two_sum import two_sum

def test_basic():
    assert two_sum([4, 2, 0, 11], 15) == [0, 3]

def test_no_pair():
    assert two_sum([1, 2, 3], 18) == []

def test_empty():
    assert two_sum([], 5) == []

def test_duplicates():
    assert two_sum([3, 3], 6) == [0, 1]