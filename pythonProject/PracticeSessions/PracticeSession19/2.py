# Create a program  that accepts two integers from the user Handle the case where the user
# enters a non-integer value using ValueEnor
def q2(a, b):
    print(a,b)
# a='hellow'
try:
    a=int('w')
    b=33
    q2(a, b)
except ValueError :
    print('custum message ')
except Exception as e:
    print(e)
