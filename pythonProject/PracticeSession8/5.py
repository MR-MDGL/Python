# Remove Dictionary Keys That Are in a Set
dict1={'a':10,'b':20,'c':30}
set1={'a','b'}
def removeKey(dict1,set1):
    for key in set1:
        if key in dict1.keys():
            dict1.pop(key)
    print(dict1)
removeKey(dict1,set1)