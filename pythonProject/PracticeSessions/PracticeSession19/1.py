# 1. Write a program to divide two numbers. Handle the case where the divisor is zero using
# ZeroDivisionError
def div(a,b):
    if a==0 or b==0:
        raise ZeroDivisionError('custum message')
    if a>0 and b>0:
        print(a/b)
    else:
        print('custum message from else part of function ')
a=0
b=2
try:
    div(a,b)
except ZeroDivisionError as c:
    print(c)
except Exception as e:
    print(e)


