# Implement a function to check if a number is even or odd and returns a boolean value.
def oddOrEven(n):
    if n%2==0:
        return True
    else:
        return False
n=int(input("enter a number to cheack if number is even or odd"))
print(oddOrEven(n))
