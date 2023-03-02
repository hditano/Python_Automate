import pytest


class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, change_salary=0):
        if change_salary:
            self.annual_salary += change_salary
        else:
            self.annual_salary += 5000

    def show_employee(self):
        return f'{self.first_name} {self.last_name} | {self.annual_salary}'


my_employee = Employee("Hernan", "Di Tano", 5000)
my_employee.show_employee()
