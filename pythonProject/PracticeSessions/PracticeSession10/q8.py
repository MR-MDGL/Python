# Write a recursive function to find the nth Fibonacci number.
# n=int(input("enter nth num you want to find"))

def fibonum(n):
    if n==1:
        return 0
    elif n==3 and n==2:
        return 1
    else:
        return fibonum(n-2) + fibonum(n-1)

print(fibonum(5))