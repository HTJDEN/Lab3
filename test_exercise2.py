import Lab2.exercise2 as exercise2

def test_find_min_max():
    actual_max = 6
    actual_min = 1
    test_input =  [1,2,3,4,5,6]
    
    result = exercise2.find_min_max(test_input)

    assert (result[0] == actual_min)
    assert (result[1] == actual_max)

def test_calc_average():
    test_input =  [1,2,3,4,5,6]
    actual_average = 3.5
    result = exercise2.calc_average(test_input)
    assert (result == actual_average)

def test_calc_median_temperature():
    test_input = [1,2,3,4,5,6]
    sorted_list = [1,2,3,4,5,6]
    actual_median = 3.5
    result = exercise2.calc_median_temperature(test_input, sorted_list)
    assert (result == actual_median)
