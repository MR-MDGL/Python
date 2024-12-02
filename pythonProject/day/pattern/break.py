n=15
for i in range (1,n+1):
    if( i==5):
        print("contune called for i=",i)
        continue
    if(i==10):
        print("break called for i=",i)
        break
    print(i)
