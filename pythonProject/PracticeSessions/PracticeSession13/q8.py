# 8.Create a class Employee that overrides str to format the details.

class Emp():
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    def __str__(self):
        return (f'{self.name} {self.sal}')

e1=Emp('sunil',200000)
print(e1)