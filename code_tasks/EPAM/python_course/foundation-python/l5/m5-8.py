"""Modifications."""


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


# "First object of Employee class"
emp1 = Employee("Slave", 200)

# "Second object of Employee class"
emp2 = Employee("Master", 5000)
emp1.display_employee()
emp2.display_employee()
print(f"Total Employee: {Employee.emp_count}")






emp1.age = 7 # Add an 'age' attribute.
emp1.age = 8 # Modify 'age' attribute.
del emp1.age # Delete 'age' attribute.
# Returns true if 'age' attribute exists
hasattr(emp1, 'age')
# Returns value of 'age' attribute
getattr(emp1, 'age')
# Set attribute 'age' at 8
setattr(emp1, 'age', 8)
# Delete attribute 'age'
delattr(empl, 'age')