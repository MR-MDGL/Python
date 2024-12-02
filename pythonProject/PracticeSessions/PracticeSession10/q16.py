# Write a function that takes a list of numbers and returns both the maximum and minimum numbers.
list1=list(map(int,input("enter value of list").split(",")))
print(list1)
def maxMin(list1):
    max=float('-inf')
    min=float('inf')
    for i in list:
        if i>max:
            max=i
        if i<min:
            i=min
        return max,min
print(maxMin(list1))
