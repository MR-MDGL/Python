# Check if a Set of Keys Exists in a Dictionary
dict1={'a':10,'b':20,'c':30}
set1={'a','b','c'}
for  key in dict1.keys():
    if key in set1:
        print(f"true for {key}")
    else:
        print(f'false for {key}')
