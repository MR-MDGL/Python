# # factorial using recursion
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
#
# print(fact(4))
#




# def sum(n):
#     if n==1:
#         print("base condition met",n)
#         return 1
#         # break
#     else:
#         print(n)
#         return n+sum(n-1)
# print(sum(4))






# even from list
# list1=[9,8,7,6,5,44,42,98,4,3,2,1]
# even_no=list(filter(lambda x:x%2==0,list1))
# print(sorted(even_no,key=None,reverse=True))


# print list according to len of city name
# list1=['punjab','haryana','delhi','chandigarh','bihar','rajesthan']
# # def len_city(list1):
# #     return len(list1)
# #
# # sort=sorted(list1,key=len_city,reverse=True)
# # print(sort)
#
# sort2=sorted(list1,key= lambda x:len(x))
# print(sort2)



# square of values from a list
# list1=[2,3,4,5,6]
# def pow(list1,pow):
#     square = list(map(lambda x: x ** pow, list1))
#     # print(square)
#     return square
# print(pow(list1, 3))


# def hellow(*a,**b):
#     print(a)
#     for key,value in b.items():
#         print(key,value)
# hellow('sunil','aman','satvinder',name='satvinder',age="24",name1="aman",age1="23")


names=tuple(['satvinder','aman','sunil'])
def fun(*names):
    








