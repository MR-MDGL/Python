'''
class Myclas():
    def myfun(self):
        pass
    def displayHellow(self):
        print("hellow")
    def display(self,name,age):
        print(name,age)

# create object
obj1=Myclas()
# obj2=Myclas()
# obj3=Myclas()


obj1.display("name",22)
obj1.displayHellow()


'''

class Myclas():
    def fun1(self):
        print("this is insstance method")

    @staticmethod
    def fun2(num):
        print(num)

obj1=Myclas()

