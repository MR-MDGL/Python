# Merge Two Sets and Add Their Elements as Keys in a Dictionary
set1={'a','b','c'}
set2={'d','e','f'}
set3=set1.union(set2)
dict1={}
for i in set3:
    dict1[i]=None
print(dict1)
