# Create a class person attributes name and age derive class employee from person that adds employee id
# and salary implements method to display details of both classes
class Person():
    def __init__(self,name ,age):
        self.name=name
        self.age=age
class Employee(Person):
    def display_employee_information(self,empid):
        print(f'name is {self.name}\nage is {self.age} \nemp id is {empid}')

ob1=Employee('sunil','23')
ob1.display_employee_information('E007')