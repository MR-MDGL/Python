# # copy elements in list
# ls1=[1,2,3,4]
# ls2=list(ls1)
#
# ls3=ls1.copy()
# print(ls3, "copy ")
#
# #combine + join
# ls4=ls1+ls2
# print(ls4,"using +")
# ls5=["this is list 5"]
# for i in ls4:
#     ls5.append(i)
# print(ls5)
from audioop import reverse

#-------------------------------------input from user
# newlist=input("enter list").split(" ")
# print(newlist)


#-------reading a list of no from uer input
# a=list(map(float,(input("enter value for int").split(" "))))
# print(a)


#---------------sorting on list

list1=[10,45,75,39]
# print(list1.sort())

#----reverse
list1.sort(reverse=True)
print(list1)
# DeprecationWarning: 'audioop' is deprecated and slated for removal in Python 3.13
#  from audioop import reverse
#(warning says that this functionality is not supported in latest version )



