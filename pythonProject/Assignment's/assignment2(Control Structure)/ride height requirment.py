def childride(height,adult):
    if (height>=48):
        print("you can ride")
    elif(42<=height>=47 and adult==True):
        print("ride with adult")
    else:
        print("go home kid")

height=int(input("enter height"))

adult=bool(input("is adult with child enter 1 for yes and 0 for no"))
childride(height,adult)