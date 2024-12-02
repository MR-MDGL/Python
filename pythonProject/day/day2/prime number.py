# find that entered num is prime or not
n=int(input("enter a number"))
var=True
half=int(n/2+1)
for i in range(2,half):
    if(n%i==0):
        var=False
        break



if var:
    print("prime ")
else:
    print("not Prime")
