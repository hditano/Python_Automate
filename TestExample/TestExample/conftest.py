from employee import Employee
import pytest


@pytest.fixture(scope="session")
def my_test():
    my_test_employee = Employee("Hernan", "Di Tano", 5000)
    return my_test_employee
