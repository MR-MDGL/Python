s='sunil'
print(s.capitalize())       #captilise first char only

print("WELCOME".lower())

print(s.swapcase())     #upper to lower and vice versa

print(s.replace("l","l sharma"))

#reverse string
#using for loop
str="abcder"
revstr=""
for i in str\
        :
    revstr=i+revstr
print(revstr)


#reverse using slicing
name="aman"
revname=""
revname=name[::-1]
print(revname)