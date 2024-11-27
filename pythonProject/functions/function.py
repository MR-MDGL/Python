# functions are piece of code contain set of instrunctions
# easier to debug
# python supports
from functools import reduce                # for reduce function in line 210

# def function(name,surname):
#     print("hellow",name)
#
# function("sunil",1)
# print(function())

# def function(a,b):
#     return a+b
#
# print(function(10,20))


# ------------------------------------------------------
# def function():
#     return
# print(function())


# -------------------------------two types of function return type or print type--------------
# return type
# def function(a,b):
#     return a+b
#
# print(function(10,20))


# print type
# def function(a,b):
#     print(a+b)
#
# function(10,20)

# catogary of function
# no argument not return any value ------None
# fun don't take argumetn but return some value
# take argument nut no return value -------print()
# fun take argument and also return value

#-------------------- add using two num
# def sum(a,b):
#     return a+b
# print(sum(10,20))


#       factorial using function
# def fact(n):
#     ans=n
#     while (n != 1):
#         ans*=n-1
#         n-=1
#     return ans
# n=int(input('enter number'))
# print(fact(n))


# scope of variable
# local inside function



# --------------------------global             define
# globalvar=10 # global variable
# def fun():
#     local=20
#     print(local,globalvar)
# fun()



# ------------------when global and local are same name
# ab=20
# def fun():
#     ab=10
#     print(ab)
# fun()


# -------------------------req is we want to change value of global
# xy=100
# def cool():
#     global xy                   # here we can acces the global variable using 'global' keyword
#     xy=200
#     print(xy)
# print(xy)       #100  becuse cool not called
# cool()          #200  changed global's value
# print(xy)       #200  global's new value after change



# --------its not mandatory to declare outside function we can also declare it inside function
# def fun():
#     global a
#     a=100
# print(a)            #give error
# fun()               # global variable created
# print(a)            #a= 100


# -----------------------------argument types
# 1 positional argument
# 2 keyword
# 3 default




# eg1---
# def fun(i,j):
#     print(i,j)
# fun(10,20)      #positional argument
#
# # keyword argument
# fun(j=200,i=100)       #keyword argument


# eg2---default value assigned to positional argument
# def fun(i,j=200):                 #default argument
#     print(i,j)          # default value is 200 if user asign new value it replaces itself with new value
# fun(10,300)     # here secondary value isn't mandatory


# -------------------------------------------------------------example using all--------------------------------
# def greet(name,greet='key how are you '):               #greet has default argument
#     print(greet,name)
# greet("sunil","good morining")      #positional argument
# greet(name="sunil",greet='hellow')              #keyword argument
# greet(name="sunil")                             #use to show default argument



# --------example
# def fun(a,b,c):
#     print(a,b,c)
# fun(10,20,30)
# fun(10,c=30,b=20)
# # fun(c=30,b=20,10)   # we cant have keyword value first and then default


# ----greatest of two num
# def greatest(a,b):
#     if a>b:
#         print(a)
#     else:
#         print(b)
# greatest(10,20)




#---------------------------------------------------------lambda function------------------------------------------
# x= lambda a:a+10
# print(x(5))
#
# x= lambda a,b:a*b
# print(x(5,5))
# lambda is generally used with filter,sort


# function to get even from list
# list1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def getEven(list1):
#     ans=[]
#     for i in list1:
#         if i%2==0:
#             ans.append(i)
#
#     print(ans)
# getEven(list1)


# --------using lambda
# list1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_no=list(filter(lambda  x:x%2==0,list1))
# print(even_no)



#
# city=['jaipur','bhiwani','patiala','kota','delhi']

# def length(city):
#     return  len(city)
# sort=sorted(city,key=length,reverse=False)
# print(sort)

# using lambda
# sort=sorted(city,key=lambda x:len(x),reverse=False)
# print(sort)








# -------------------------lambda with map function
# no=[1,2,3]
# square=list( map( lambda x:x**2 , no))
# print(square)



# -------------------------reduce function
# z=reduce( lambda x,y:x+y, [1,2,3,4,5])
# print(z)
# disadvantage of lambda
#  lambda is not suitable for multiple expressions
#








# -------------zip()        returns data into tuple fromat
# a = [10, 20, 30, 50]
# b = [40, 50, 60]
#
# zipped = zip(a, b)
# print(type(zipped), list(zipped))




# eg2
# subject=['english',"maths",'science']
# marks=[10,24,55]
# a=zip(subject,marks)
# print(list(a))




