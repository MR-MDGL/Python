# q5 code that removes the min and max values from a set
# from sys import float_info
set1={10,200,30,40}
min=float("inf")
max=float("-inf")
for i in set1:
    if i<min:
        min=i
    if i>max:
        max=i
print(min,max)
# print(type(set1))
set1.remove(min)
set1.remove(max)
print(set1)