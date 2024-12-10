from abc import ABC,abstractmethod

class Shape(ABC):
    def __init__(self,w,h):
        self.width=w
        self.height=h
    @abstractmethod
    def area(self):
        pass
    def parameter(self):
        pass
class Rectangle(Shape):
    def area(self):
        print(f'area is {self.width*self.height}')
    def parameter(self):
        print(f'parameter is {2*(self.height+self.width)}')
ob=Rectangle(20,30)
ob.area()
ob.parameter()