number = int(input("enter a number"))
backup = number
sum = 0
count = 0
length=0
#length
while(number > 0):
    number = int(number / 10)
    count+=1
num2=backup
while(num2 > 0):
    power=int(num2 % 10)

    num2= int(num2 / 10)
    length=count
    temp = 1
    while(length > 0):
        temp*=power
        length-=1
    sum+=temp
print(sum == backup)

