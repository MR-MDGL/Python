# Task 14
#
# Write a program that takes three numbers as input and prints the largest of the three.

a=int(input("enter a"))

b=int(input("enter b"))

c=int(input("enter c"))

if a > b and a >c:
    print("a is greatest")
elif b>a and b>c:
    print("b is greatest")
else:
    print("c is greatest")