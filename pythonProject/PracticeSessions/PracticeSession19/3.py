# 3. Write a progam that accepts a list of integers from the user and retrieves an element by
# index. Handle the case where the index is out of range using IndexError.
list1=map(int,input('values from list ').split(','))
index=int(input('enter index'))
def findidx(list1,index):
    if index in list1:
        return (index)
    if index not in list1:
        raise IndexError

try:
    print(findidx(list1,index))
    # raise IndexError

except  IndexError:
    print('custum exception')
except Exception as e:
    print(e)



