# 2. Write a Python program to demonstrate single inheritance using a Person class and a derived class Employee.
class Person():
    def display(self):
        print('person class')
class Employee(Person):
    pass
o=Employee()
o.display()