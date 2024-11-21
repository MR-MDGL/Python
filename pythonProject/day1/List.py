# list
from operator import is_not

x=[1,2,3,4,]        #list
y=x     # contains address of x  || y is also a referance  variable

z=[1,2,3,4,5,]      #entire different list



# to cheack if x and y both are pointing to the same Refernece by using identity opereator
# is/is not
# print(x is y)#true
# print(x is not y)#false
# print(x is not z)
# print(x is z)




# differance between 'is' & '=='
# == compares values only
# is compares references only

a=10
b= 10

print(a == b)
print(a is b)
