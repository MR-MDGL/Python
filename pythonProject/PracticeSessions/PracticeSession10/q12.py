# Write a lambda function with map to double the elements of a list.
list1=list(map(int, input('enter list').split(",")))
# print(list1, type(list1))
double=list(map(lambda x: x * 2, list1))
print(double)