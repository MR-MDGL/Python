# from struct import pack_into
#
# tp1=(1,2,3,4,5,6,"seven",8.0,"IX")
# print(tp1)
#
#
#
# # tp1[2]="index2"
# # print(tp1)          #cant change any index
#
# # tp1.append("last")        #gives AttributeError: 'tuple' object has no attribute 'append'
# print(tp1)
#
#
tupple1=(1,2,3)
# tupple2=(4,5,6)
# print(tupple1+tupple2)
#
#
# print(len(tupple2),"is length of tupple2")
#
#
#
# # creating with tuple() constructor
# newtp=tuple(("apple","mango","banana"))
# print(type(newtp),newtp)
#
#
#
#

newlist=list(tupple1)
print(newlist)

newlist[2]="two"
newtuple=tuple(newlist)
print(newtuple)

#looping tuple
for i in newtuple:
    print(i,end=" ")





