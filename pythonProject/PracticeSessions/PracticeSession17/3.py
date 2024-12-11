
# 3. Create a base class Shape with a method area. Derive classes Rectangle and Circle from Shape and
# implement the area method for each.
class Shape():
    def __init__(self,l,b):
        self.length=l
        self.bredth=b
class Rectangle(Shape):
    def area(self):
        print(f'{self.bredth*self.length}')
o=Rectangle(2,3)
o.area()