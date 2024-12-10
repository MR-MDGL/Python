# inheritance  having attributes of another class
# code reusability and avoid duplication
#-------------------------------types
#single         1 parent   1 child
# multilevel     multi level of parent child
# multiple      2 parent 1 child
#hieraricy      1 parent multiple child






# print('--------------single inheritance-----------')
# class A:
#     def __init__(self):
#         print('constructor called')
#     def m1(self):
#         print('method from class A')
# class B(A):
#     def __init__(self):
#         print('derived class constructor')
#     def m2(self):
#         print('method from class B')
# obj=B()
# obj.m2()
# obj.m1()
# print()
# print()
# print()







# print('-------------multilevel inheritance-----------')
# class A:
#     x,y=10,20
#     def m1(self):
#         print('method from class A')
# class B(A):
#     a,b=100,200
#     def sum(self):
#         print('sum is ',A.x+B.y)
#     def m2(self):
#         print('method from class B')
# class C(B):
#     def m3(self):
#         print('method from class C')
# obj=C()
# obj.m1()
# obj.m2()
# obj.m3()
# print()
# print()
# print()
# print()












# print('-------------hierical inheritance-----------')
# class A:
#     x,y=10,20
#     def m1(self):
#         print('method from class A')
# class B(A):
#     a,b=100,200
#
#     def m2(self):
#         print('method from class B')
# class C(A):
#     def m3(self):
#         print('method from class C')
# obj=C()
# obj.m1()
# obj.m3()
# obj1=B()
# obj1.m1()
# obj1.m2()





# print('--------------multiple inheritance----------')
# #a and b are parent here and c is child for a and b
# class A:
#     x,y=10,20
#     def m1(self):
#         print('method from class A')
# class B():
#     a,b=100,200
#
#     def m2(self):
#         print('method from class B')
# class C(A,B):
#     def m3(self):
#         print('method from class C')
# ob=C()
# ob.m1()
# ob.m2()
# ob.m3()



# #example only
# print('--------------multiple inheritance example for the preferance ----------')
# #a and b are parent here and c is child for a and b
# #here A is first and B is second here m is the same method in both classes
# # if we call ob.m this will give prefrance based on the oder which was given on the child class here it is (A,B)
# class A:
#     def m(self):
#         print('method from class A')
# class B():
#     def m(self):
#         print('method from class B')
# class C(A,B):
#     def m3(self):
#         print('method from class C')
# ob=C()
# ob.m()
# ob.m()
