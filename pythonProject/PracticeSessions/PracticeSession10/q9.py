# Implement a recursive function to calculate the sum of the digits of a given number.
# n=1234
n=int(input("enter your number "))

def sum_of_digit(n):
    if n<=0:
        return 0
    else:
        last_digit=n%10
        n//=10
        return last_digit+(sum_of_digit(n))
print('sum is ',sum_of_digit(n))