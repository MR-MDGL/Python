# n=int(input("enter value of n "))
#
# n=5
# for i in range(n-1):            # -----------first half-----------
#     for j in range(n-i-1):
#         print(" ",end= " " )
#     for j in range(i+1):
#         print("x",end= " " )
#     for j in range(i):
#         print("x",end= " " )
#     print()
# print()
# for i in range(n):              # ------------other half------------
#     for j in range(i):
#         print(" ",end= " " )
#     for j in range(n-i):
#         print("x",end=" ")
#     for j in range(n - i-1):
#         print("x",end= " " )
#     print()
#
#         x
#       x x x
#     x x x x x
#   x x x x x x x
# x x x x x x x x x
#   x x x x x x x
#     x x x x x
#       x x x
#         x







#done by me
n=5
for i in range(n-1):            #----------first half----------
    for j in range (n-1-i):
        print(" ",end=" ")
    for k in range (i):
        print("*",end=" ")
    for k in range (i+1):
        print("*",end=" ")
    print()
for i in range(n):              #---------second half------
    for j in range (i):
        print(" ",end=" ")
    for k in range(n-i):
        print("*",end=" ")
    for k in range(n-i-1):
        print("*",end=" ")
    print()