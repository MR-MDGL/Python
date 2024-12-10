#define class shape with method area() that raise a NonImplementationErro
#create sub class rectangle and circle implement the area method
# class Shape():
#     def area(self):
#         raise NotImplementedError('subclass must implement this method')
# class Rectangle(Shape):
#     def __init__(self,areaval):
#         self.areaVal=areaval
#     def area(self):
#         print(f'area method from class Rectangle value is {self.areaVal}')
# class Circle(Shape):
#     def __init__(self,areaval):
#         self.areaaval=areaval
#     def area(self):
#         print('area method from class Circle',self.areaaval)
#         Rectangle.area(self)
#
# shapes=[Rectangle(20),Circle(15)]
# for shape in shapes:
#     shape.area()
#



class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement this method")

class Rectangle(Shape):
    def __init__(self, areaval):
        self.areaval = areaval

    def area(self):
        print(f"Area method from class Rectangle. Value is {self.areaval}")

class Circle(Shape):
    def __init__(self, areaval):
        self.areaval = areaval

    def area(self):
        print(f"Area method from class Circle. Value is {self.areaval}")

shapes = [Rectangle(20), Circle(15)]

for shape in shapes:
    shape.area()



