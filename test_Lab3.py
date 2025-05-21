import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]
    assert Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING) == test_arr
    # def test_bubble_sort_ascending():
    # result = []  # optional init, not strictly needed
    # input_arr = [64, 34, 25, 12, 22, 11, 90]
    # test_arr = [11, 12, 22, 25, 34, 64, 90]  # expected result

    # result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    # assert (result == test_arr)

def test_bubble_sort_descending():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    assert Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING) == test_arr
# def test_bubble_sort_ascending():
#     result = []  # optional init, not strictly needed
#     input_arr = [64, 34, 25, 12, 22, 11, 90]
#     test_arr = [11, 12, 22, 25, 34, 64, 90]  # expected result

#     result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

#     assert (result == test_arr)

def test_bubble_sort_invalid():
    # assert Lab3.bubble_sort([], Lab3.SORT_DESCENDING) == 0
    # assert Lab3.bubble_sort([], Lab3.SORT_ASCENDING) == 0
    result = Lab3.bubble_sort([], Lab3.SORT_DESCENDING)
    assert result == 0

def test_bubble_sort_too_many_elements():
    assert Lab3.bubble_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], Lab3.SORT_DESCENDING) == 1
    assert Lab3.bubble_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], Lab3.SORT_ASCENDING) == 1

def test_bubble_sort_wrong_elements():
    assert Lab3.bubble_sort([3, 2, 'a', 1], Lab3.SORT_DESCENDING) == 2
    assert Lab3.bubble_sort([3, 2, 'a', 1], Lab3.SORT_ASCENDING) == 2
