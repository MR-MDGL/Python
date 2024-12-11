# error
# syntax mistake in syntax          occour at compile time
# logic sementic error problem with logic where expected ouptu does't meet the actuale      compile time
# runtimeerroe                  errors that are gentate duting the execution of the program unexperctd erroes
                        #unsucessfull termination of code
# from ctypes import c_ushort


#as programmmer our job is to execute the program with our without exception this is called exception handalling
# we use try and  except
# try code that might cause exception
# except----except Exception as e:
# else:-----
#finally ---any default code to execute exception occoured or not doesnot matter
# code to execute


#we can write multipple except blocks






# #example usage
#
# print('Hellow')
# try:
#     print(10 / 0)
#     #we can have one try block but multipple except blocks
# except FileNotFoundError:
#     print('file not found exception lien 32')
# except ZeroDivisionError:
#     print('zero divisi')
# except Exception as e:
#     print('exception type is: ',e)
# finally:
#     print('this is the default message from finally')
# print('Hellow')


#example 2
# try:
#     # Code with intentional runtime error
#     eval("if True print('Invalid syntax')")
# except SyntaxError:
#     print("A syntax error occurred! Please check your code.")

# try:
#     # Intentionally incorrect syntax (missing colon)
#     if True
#         print("This won't execute due to the syntax error.")
# except SyntaxError:
#     print("A syntax error occurred! Please check your code.")






# # ----------------------raiseing our own exception
# def enterage(num):
#     if num <0:
#         raise ValueError #('default exception line 64 ')
#
#     if num%2==0:
#         print('even')
#     else:
#         print('odd')
# n=-1
# try:
#     enterage(n)
# # except ValueError:
# #     print('custum message from ValueError')
# except Exception as e:
#     print(e,'default exceptionline 77')
# print('blah blah')









#----------custum exception
# class custuomException(Exception):
#     pass
# try:
#     raise custuomException('custum error occoured ')
# except custuomException as e:
#     print(e)














#------------custum exception class
class NegiveNumberError(Exception):
    def __init__(self,msg='negetive values are not allowedthis is custum message'):
        self.msg=msg
        super().__init__(self.msg)

def cheackPositiveNum(number):
    if number<0:
        raise NegiveNumberError()
    else:
        print(f'number is {number} positive ')

try:
    n1=-1
    cheackPositiveNum(n1)
except NegiveNumberError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)




