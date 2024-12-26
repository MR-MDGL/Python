# n=4
# fact=1
# for i in range (1,n+1):
#     fact*=i
# print(fact)


def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)


print(fact(4))