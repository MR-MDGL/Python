# create a class calculator with an instance method (self,a,b) to add two numbers now add a static method
# to print 'this is a calculator class' Call both methods

class Calculator():
    def add2num(self,a,b):
        return a+b
    @staticmethod
    def info():
        return ('this is a calculator class')

obj1=Calculator()
print(obj1.add2num(20,30))
print(obj1.info())