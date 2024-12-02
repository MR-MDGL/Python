s1=int(input("enter marks out of 100"))
s2=int(input("enter marks out of 100"))
s3=int(input("enter marks out of 100"))
s4=int(input("enter marks out of 100"))
s5=int(input("enter marks out of 100"))


def grades(a,b,c,d,e):
    sum=a+b+c+d+e
    if sum/5>90:
        return "A"
    elif sum/5>80:
        return "B"

print(grades(s1,s2,s3,s4,s5))
