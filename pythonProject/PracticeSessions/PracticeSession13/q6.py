# 6.Create a class Shape with a default consumctor that initializes type to "Generic"

class Shape():
    def __init__(self,name):
        self.name=name
        self.type='Generic'
        # print (self.name,self,type)
    def display(self):
        return (f'your shape is {self.name} and type is {self.type}')
rectangle=Shape('rectangle')
print(rectangle.display())