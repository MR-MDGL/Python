year=200
if(year%400==0):
    print("leap")
elif(year%100==0):
    print("leap")
elif(year%4==0):
    print("leap")
else:
    print("normal year")