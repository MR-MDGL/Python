#6. Create a point class to represent a point in 2D space with attnbutes x and y. Use constructor to initialize these
# values and a method to calculate the distance betv.een two points.
import math
class Point():
    def __init__(self,x1,y1,x2,y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
    def distance(self):
        ans=(   (self.x2- self.x1)**2   )    +   ((   self.y2 - self.y1    )**2)
        finalans=math.sqrt(ans)
        print(f'final ans is {finalans}')

ob1=Point(3,7,4,1)
ob1.distance()
