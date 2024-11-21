n=5
count=1
for i in range(n+1):
    #space
    for j in range(n-i):
        print(" ",end="")
    for k in range (i):
        print(f"{ count:2}",end=" ")
        count+=1
    print()