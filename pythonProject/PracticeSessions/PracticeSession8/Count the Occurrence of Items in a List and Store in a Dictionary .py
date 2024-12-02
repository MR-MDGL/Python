# Count the Occurrence of Items in a List and Store in a Dictionary
list1=[1,2,3,4,5,1,2,3]
dict1=dict()
for i in list1:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1
print(dict1)





