mySet={1,2,3}
#set doesnot support indexing
# set cant have duplicate items
# sets are mutable      but elements are immutable          we can append or delete items but cant change perticluar item
# support add()  update()   length()
# remove()      throws error if element isn't available in set
# discard()     discard will not throw error if not in set
# methods
# print(mySet[2])       #TypeError: 'set' object is not subscriptable
mySet.add(4)
print(mySet)
# mySet.remove(3)
print(mySet)
mySet.pop()     #removes first element
print(mySet,"after pop called")
# mySet.update()
#
# list2=list(mySet)
# print(list2)

newset={1,2,3,4,5,6,7,8}
newset.remove(3)
print(newset,newset)
# newset.discard()




# ---------------union
# | --> union
set1={1,2,3,4}
set2={3,4,5}
# print(set1.union(set2))
print(set1 | set2,"union with symbol |")

# intersections         intersection gives common in both set's
print(set1.intersection(set2),"using intersection")

print(set1.difference(set2),"difference in set's")
print(set2.difference(set1),"difference in set's")      # here the oder matters

# ---------------symetric difference
print(set1.symmetric_difference(set2),"symetric difference")

# -------------frozen set this is immutable version of set supported in python only
print(mySet,"myset")
frozen=frozenset(mySet)
print(frozen)
# frozenset.add(15)             #AttributeError: 'frozenset' object has no attribute 'add'

# -----------list method used to typecast set to list
newlist=[1,2,3,4,5]
newset=set(newlist)
print(newset,"this is newset")
print(type(newset))