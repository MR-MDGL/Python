class Company():
    companyname='BEBO Technologies'
    def __init__(self,emp_name,designation):
        self.emp_name=emp_name
        self.designations=designation

    def display(self):
        print(f'hey {self.emp_name} your designation is {self.designations} and  you work at {Company.companyname}')

emp1=Company('Sunil Mudgil','Automation Tester')
emp1.display()
