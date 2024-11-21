n=int(input("enter a number"))
count=1
for i in range(n+1):
    #space
    for j in range(n-i):
        print(" ",end='')
    #number
    for k in range(i):
        print(count,end=" ")
        count+=1

    print()


 #    1
 #   2 3
 #  4 5 6
 # 7 8 9 10

