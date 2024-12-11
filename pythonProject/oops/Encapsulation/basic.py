# encapsulation is the concept of bundling data (attributes) and the methods (functions)
# that operate on that data within a single unit, known as a class.
# @property     getter for variables
# @varname.setter             is used to set values of private variables
class A:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    #getter for name and age
    @property
    def name(self):
        return self.__name
    @property
    def age(self,new_age):
        self.__age=new_age

    @name.setter
    def name(self,new_name):
        self.__name=new_name
    @age.setter
    def age(self,new_age):
        self.__age=new_age

    def display(self):
        print('name is: ',self.__name,'\nage is: ',self.__age)
o=A('sunil', 23)
o.display()
o.name='ram'
o.age=99
o.display()


