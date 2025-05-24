import employee_info as employee

def test_get_employees_by_age_range():      
    input_age_lower_limits = 20
    input_age_upper_limits = 40

    result = employee.get_employees_by_age_range (input_age_lower_limits , input_age_upper_limits)
    for item in result:
        assert (20< item["age"] < 40)
    
def test_calculate_average_salary():
    actual_salary = 8333.333333333334
    result = employee.calculate_average_salary()
    assert (result == actual_salary)

def test_get_employees_by_dept():
    department = "Sales"
    result = employee.get_employees_by_dept(department)
    for items in result:
        assert items["department"] == department
    

