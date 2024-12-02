# Find Common Values Between Two Dictionaries Using Sets
dict1={'a':10,'b':20,'c':30}
dict2={'d':20,'e':30,'f':40}

set1=set(dict1.values())
set2=set(dict2.values())
print("common values are",set1 & set2)
