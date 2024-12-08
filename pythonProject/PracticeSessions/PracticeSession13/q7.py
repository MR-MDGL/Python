# 7.Create a class Rectangle with a method to calculate and return the area.

class Rectangle():
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def display(self):
        print(f'area is {self.l*self.b}')

r1=Rectangle(20,30)
r1.display()
