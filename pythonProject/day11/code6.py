# q7 code  that finds index of all occurences of a specific element in a list
# using the index method if the elemnt is not found return None
list1=[1,2,5,3,4,5,6,5]
target=5
list2=[]

# def findIndex(list1,find):
#     list2 = []
#     for i in list1:
#         if find not in list1:
#             return None
#         if list1[i] == target:
#             list2.append(i)
#
#
#     return list2
# print(findIndex(list,target))


for i in  range(0,len(list1)):
    if target not in list1:
        print("none")
        if list1[i] == target:
                list2.append(i)
        # print()
    # return list1.index(i)
    #  str.append(list1.index(i))
print(list2)
# khhgh


