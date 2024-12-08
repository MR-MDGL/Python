class Employee():
    def __init__(self, id, name, sal,raisepercentage):
        self.id = id
        self.name = name
        self.sal = sal
        self.raiseper=raisepercentage



    def raiseSal(self):
        r=(self.sal * self.raiseper)/100
        totalraise=r+self.sal
        print(f'hey {self.name} your emp id is {self.id} salary is {self.sal} and your salary after raise is {totalraise}')
emp1=Employee('007','sunil',100,15)
emp1.raiseSal()