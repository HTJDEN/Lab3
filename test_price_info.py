import price_info as price

def test_total_cost_shopping():
    expected_total = 46.75
    assert price.total_cost_shopping() == expected_total

def test_cost_of_fruits():
    expected_total = 12.0
    assert price.cost_of_fruits('apple', 10) == expected_total