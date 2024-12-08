class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f'hey {self.name} you are {self.age} now')
ob1=Person('sunil',23)
ob1.display()
ob2=Person('ram',23)
ob2.display()
