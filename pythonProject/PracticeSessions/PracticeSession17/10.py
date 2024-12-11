# 10. Implement a program to show how to prevent instantiation of an abstract class.
from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def display(self):
        pass
class B(A):
    def display(self):
        print('display method from class B')
o=B()
o.display()
# o1=A()
# o1.display()