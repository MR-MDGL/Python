# create and print sum of arrays
from functools import reduce
import array as arr



# 1
# arr1=arr.array('i',[1,2,3,4,5,6,7,8,9,10])
# for i in arr1:
#     print(i,end=" ")


# 2 sum 3 max min
arr1=arr.array('i',[1,2,3,4])
print(type(arr1))
def sumarr(arr):
    sum=0
    max=float('-inf')
    min=float('inf')
    for j in range (0,len(arr1)):
        if arr[j]>max:
            max=arr[j]
        if arr[j]<min:
            min=arr[j]

        sum += arr[j]
    print(f'sum is {sum} max is {max} minn is {min}')



sum=reduce(lambda a,b:a+b,arr1)
print('sum using lambda is ',sum)


sumarr(arr1)