# q6 find out the symetric difference of two sets
set1=set(map(int,input("enter value").split(',')))
set2=(map(int,input("enter value").split(',')))
# print(set1,set2)
print(set1.symmetric_difference(set2))            #method1
# print(set1^set2)                                  #method2