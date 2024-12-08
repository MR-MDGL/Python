# create a class book employee with variable name and salary add method update salary to
# modify the salary of employee display it using another method
class Employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def updateSalary(self,new_salary):
        self.salary=new_salary
        print (f"Employeee name is {self.name} and updated salary is {self.salary}")
    def display_salary(self):
        print(f"Employeee name is {self.name} and current salary is {self.salary}")


sunil=Employee('sunil',10000)
sunil.display_salary()
sunil.updateSalary(200000)
sunil.display_salary()


