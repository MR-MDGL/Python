#complex
import math

a=3+4j
print(type(a))
'''
types of xonversion
implecit
    by compiler itself 
        eg a=10     compiler will be convert a to float
            b=2.3
            print(a+b)
explicit
    eg int(),float(),complex(),bool()
    
    
    
    
    absolute abs()      returens absolute values
    rount() rounds numnber upto specific value 
    print(round(4.5))       output will be 5

'''

a = 10
b = 2.3


print(round(4.5))

#power functin
print(pow(2,3),"2 power 3 is ")

#min returens the smallst of the given num or iteratabel
print(min(3,1,4,1,5),"is minimum number ")

print(max(3,1,4,1,5),"is max number ")

print(sum([3,1,4,1,5]),"is sum number ")        #[] is a list

print(sum((3,1,4,1,5)),"is sum number ")        #() is a set

#divmod method returns a tuple one is quectiot othe is reminder
print(divmod(10,3))   #  10//3=3,10%3=1

#comples creates a complex number
# is isinstance()     #weather is instance (eg of specific class
print(isinstance(4,int))
print(isinstance( 2.2,float))


n=5
result=math.factorial(n)
print("factorial is ",result)
