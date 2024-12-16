'''
working with text files
we use open() give path
'''

# # #---------writing in file
# file=open(r"E:\BEBO-Tech\Python\filehandalling.txt",'w')
# try:
#     file.write('ram\n')
#     file.write('lakshman\n')
#
# except Exception as e:
#     print(e)
# file.close()
# print('file writing successfully')
# print('------------')



# # --------reading from file
# file=open(r"E:\BEBO-Tech\Python\filehandalling.txt",'r')
# # print(file.readline())
# print('------reading file-------------')
# print(file.read())
# print(file.readable())
# print('program executed')



#
# #---------appending  in existing file
# file=open(r"E:\BEBO-Tech\Python\filehandalling.txt",'a')
# print('-----------appending on to exisiting file -------------')
# try:
#     file.write('new instruction\n')
#     file.write('new instruction\n')
#
# except Exception as e:
#     print(e)
# file.close()
# print('file writing successfully')
#
#
#
#
#
# # --------reading from file
# file=open(r"E:\BEBO-Tech\Python\filehandalling.txt",'r')
# # print(file.readline())
# print('------reading file-------------')
# print(file.read())
# print(file.readable())
# print('rading file success')









#working with os
import os
try:
    # os.remove(r"E:\BEBO-Tech\Python\hellow.txt")
    os.rmdir(r"E:\BEBO-Tech\Python\pythonProject\oops\File Handalling\tempdir4")
except Exception as e:
    print(e)
print('program executed')