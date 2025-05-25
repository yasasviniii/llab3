import employee_info as employee

def test_get_employees_by_age_range():
    test = [ {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},]
    result = employee.get_employees_by_age_range(20,30)

    assert result == test

def test_calculate_average_salary():
    test = 60166.666666666664
    result = employee.calculate_average_salary()

    assert result == test

def test_get_employees_by_dept():
    test = [{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},]

    result = employee.get_employees_by_dept("Engineering")

    assert result == test

