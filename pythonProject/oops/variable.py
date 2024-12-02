# class Myclass:
#     a,b=10,20
#     def add(self):
#         print(self.a+self.b)
#
#
#     def mul(self):
#         print(self.a*self.b)
# mc=Myclass()
# mc.add()
# mc.mul()
#





# print("----------Example4----------------")
# i,j=13,20   #global
# class MyClass1:
#     a,b = 19,50     #instance variable
#
#     def add(self,x,y):      #local variable
#         print(x,y)      #print local variable
#         print(self.a + self.b)      #instance variable
#         print(i,j)      #global variable
#
# ob2 = MyClass1()
# ob2.add(5,10)

# example5

i,j=100,200 #global


class Myclass3:
    i,j=10,20
    def add(self,i,j):
        print(i,j,'passed value')
        print(self.i,self.j,'i,j inside function')
        print(globals()['i'],globals()['j'],'global i,j')

obj=Myclass3()
obj.add(22,33)





