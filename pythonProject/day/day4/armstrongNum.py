# print armstrong number    eg 123 1 ka cube+2kacube+3kacube=
#use rev logic
n=int(input("enter a number"))
backup=n
rev=0
length=0
sum=0
while n!=0:
    rem=n%10
    sum+=rem
    rev=rev*10 + rem
    n//=10
    length+=1

print(rev, length, sum)
answer=0
print(n)
n=backup

while n!=0:
    power=n%10
    temp=1
    while length>=0:
        temp*=power
        length=length-1
    sum+=temp
print("temp is ",temp)







