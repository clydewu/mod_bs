from mod_bs import find_val

def test_no_overwrite_no_gap():
    assert find_val([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0) == 0, 'Boundary'
    assert find_val([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1) == 1, 'Boundary +1'
    assert find_val([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9) == 9, 'Boundary'
    assert find_val([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8) == 8, 'Boundary -1'
    assert find_val([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 5) == 5, 'Random'
    assert find_val([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], -1) == None, 'Smaller non-existent'
    assert find_val([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 999) == None, 'Larger non-existent'


def test_no_overwrite():
    assert find_val([1, 3, 4, 5, 8, 9, 14, 16, 20, 50], 1) == 0, 'Boundary'
    assert find_val([1, 3, 4, 5, 8, 9, 14, 16, 20, 50], 3) == 1, 'Boundary +1'
    assert find_val([1, 3, 4, 5, 8, 9, 14, 16, 20, 50], 50) == 9, 'Boundary'
    assert find_val([1, 3, 4, 5, 8, 9, 14, 16, 20, 50], 20) == 8, 'Boundary -1'
    assert find_val([1, 3, 4, 5, 8, 9, 14, 16, 20, 50], 14) == 6, 'Random'
    assert find_val([1, 3, 4, 5, 8, 9, 14, 16, 20, 50], 7) == None, 'Inner non-existent'
    assert find_val([1, 3, 4, 5, 8, 9, 14, 16, 20, 50], 0) == None, 'Smaller non-existent'
    assert find_val([1, 3, 4, 5, 8, 9, 14, 16, 20, 50], 999) == None, 'Larger non-existent'


def test_overwrite_gap():
    assert find_val([100, 101, 103, 105, 107, 1, 2, 3, 5, 6], 100) == 0, 'Boundary'
    assert find_val([100, 101, 103, 105, 107, 1, 2, 3, 5, 6], 101) == 1, 'Boundary +1'
    assert find_val([100, 101, 103, 105, 107, 1, 2, 3, 5, 6], 6) == 9, 'Boundary'
    assert find_val([100, 101, 103, 105, 107, 1, 2, 3, 5, 6], 5) == 8, 'Boundary -1'
    assert find_val([100, 101, 103, 105, 107, 1, 2, 3, 5, 6], 107) == 4, 'Overwrite Boundary'
    assert find_val([100, 101, 103, 105, 107, 1, 2, 3, 5, 6], 1) == 5, 'Overwrite Boundary'
    assert find_val([100, 101, 103, 105, 107, 1, 2, 3, 5, 6], 102) == None, 'Overwrite Inner non-existent'
    assert find_val([100, 101, 103, 105, 107, 1, 2, 3, 5, 6], 4) == None, 'Inner non-existent'
    assert find_val([100, 101, 103, 105, 107, 1, 2, 3, 5, 6], 108) == None, 'Over Overwrite Boundary non-existent'
    assert find_val([100, 101, 103, 105, 107, 1, 2, 3, 5, 6], 0) == None, 'Under Overwrite Boundary non-existent'
    assert find_val([100, 101, 103, 105, 107, 1, 2, 3, 5, 6], 99) == None, 'Under boundary non-existent'
    assert find_val([100, 101, 103, 105, 107, 1, 2, 3, 5, 6], 999) == None, 'Over boundary non-existent'

