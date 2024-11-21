# write a python code that find keys that have specific value then return keys of the same value
dict1={"a":10,"b":10,"c":20,"d":30}
find=int(input("enter to find value"))
list1=[]

for key,value in dict1.items():
    if value==find:
        list1.append(key)
print(list1)
