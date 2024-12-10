# constructor def __init__()
# two types of constructor's
# default constructor and parameterised constructor()



'''
class Myclass():
    obcount=0
    def __init__(self):
        Myclass.obcount+=1
        print("constructor called ")
        print(self)     #self contains references(addres)

a=Myclass()
b=Myclass()
c=Myclass()
d=Myclass()
'''


'''
#-------------------- parameterised consturcor
class Myclass():
    name='david'
    def __init__(self,name):
        print(name)
        print(self.name)

obj1=Myclass('sunil')
# obj1.
'''

'''
class Myclass():

    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
    def display(self):
        print(self.id,self.name,self.sal)
a=Myclass(200,'sunil',20000)
a.display()
'''



# string constructor
# class Myclass():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#
#     def __str__(self):
#         return(f"hellow {self.name} you are {self.age} now ")
#
# ob1=Myclass('sunil',23)
# print(ob1)





# another example
class Myclass():
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model


    def __str__(self):
        return(f"you have {self.brand} brand and model is {self.model}  ")

c1=Myclass('TATA','Nexon')
print(c1)

print(c1.brand)
del c1.brand
print(c1.brand)

