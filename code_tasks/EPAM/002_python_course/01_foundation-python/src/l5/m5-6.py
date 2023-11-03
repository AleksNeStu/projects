"""Class."""


class Employee:
    """Common base class for all employees"""
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def display_count(self):
        print("Total Employee %d" % self.emp_count)

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)