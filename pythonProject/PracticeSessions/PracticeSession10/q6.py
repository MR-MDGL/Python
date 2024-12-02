# Write a function that takes three parameters and demonstrates the use of default values for some of them.
def defaultFun(a=1,b=1,c=1):
    print(a,b,c)
a=int(input("enter value of a"))
b=int(input("enter value of b"))
c=int(input("enter value of c"))
defaultFun(a,b)