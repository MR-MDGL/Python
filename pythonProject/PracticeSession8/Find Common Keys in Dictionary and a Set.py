# Find Common Keys Between a Dictionary and a Set
dict={'a':10,'b':20,'c':30}
set1={'a','b'}


def findCommonKeys (dict1,set1):
    final_set =set()
    print(type(final_set))
    for key in dict1.keys():
        if key in set1:
            final_set.add(key)
    print(final_set)

findCommonKeys(dict,set1)
