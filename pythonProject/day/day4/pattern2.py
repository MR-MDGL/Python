n=int(input("enter a number"))
prev=0
next=1
temp=0
print(prev,next,end=" ")
for i in range(n-2):
    temp=prev+next
    print(temp,end=" ")
    prev=next
    next=temp
    




#print fibo upto n
#print nth fibo number