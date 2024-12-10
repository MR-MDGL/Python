#abstraction in py
# we cant create object of abstract classed
# abstract classes      contains abstract method which doesnot have body
# concrte classes
from abc import ABC,abstractmethod
#abc is abstract based classes
class A(ABC):
    @abstractmethod
    def display(self):
        None
class B(A):
    def display(self):
        print('abstract method')
    # def m1(self):
    #     print('another implementaion of m1')
    def display(self):
        print('method from class B')

class C(B):
    def display(self):
        print('method from class C')
ob=C()
ob.display()
ob.display()
ob1=B()

