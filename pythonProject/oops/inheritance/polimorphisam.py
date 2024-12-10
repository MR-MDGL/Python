#method overloading
# method overriding
# python allow overriding not overloading directly
# but we can archive overloading using other concept's'
# class A():
#     def m1(self):
#         print('method from class A')
# class B(A):
#     def m1(self):       #overriding method
#         print('method from class B')
#         super().m1()            #super invoke immediate parent class method and variables
#
# ob=B()
# ob.m1()










# class A():
#     name='class A'
# class B(A):
#     name='class B'
#
# ob=B()
# ob.m1()





#overriding example
# class Bank():
#     def rateOfIntrest(self):
#         return 0
# class SBI(Bank):
#     def rateOfIntrest(self):
#         return 20
# class PNB(Bank):
#     def rateOfIntrest(self):
#         return 30
# ob1=SBI()
# print(ob1.rateOfIntrest())
# ob2=PNB()
# print(ob2.rateOfIntrest())







print("--------------overloading---------------------")
#using keyword default arguments we can archive method orverloading
class A():
    def greet(self,name=None):
        if name is not None:
            print(f'hellow {name}')
        else:
            print(f'hellow')
ob1=A()
ob1.greet()
ob1.greet('sunil')


class Calculate():
    def sum(a=0,b=0,c=0):
        print(a+b+c)
ob1=Calculate
ob1.sum(1,2,3)
ob1.sum(1,2)










# class Shape():
#     def shape(self):
#
#     raise NotImplementedError('subclass must implement this method')
