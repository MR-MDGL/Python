
n=5
count=1
for i in range(n-1):            #----------first half----------
    for j in range (n-1-i):
        print("  ",end=" ")
    for k in range (i):
        print(f"{count:2}",end=" ")
        count+=1
    for k in range (i+1):
        print(f"{count:2}",end=" ")
        count+=1
    print()
for i in range(n):              #---------second half------
    for j in range (i):
        print("  ",end=" ")
    for k in range(n-i):
        print(f"{count:2}",end=" ")
        count+=1
    for k in range(n-i-1):
        print(f"{count:2}",end=" ")
        count+=1
    print()