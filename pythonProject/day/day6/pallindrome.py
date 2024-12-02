s="abcdef"
rev=""
# rev=s[::-1]
# if (s==rev):
#     print("true")
# else:
#     print("false")



#using for
for i in s:
    rev=i+rev
print(rev)
if (s==rev):
    print("true")
    print("false")
else:
    print("false")
