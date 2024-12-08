'''
module are collection of functions
create module           create a python file
modules         use them using import
1. builtin
2. user definese



import is workable only when both files are on the same directoary


'''
from PracticeSessions.PracticeSession10.q4 import calculateAreaOfRectangle
# using add,multiply from calculator file in the same directory

#Appraoch 1
# import calculator
# calculator.addition(10,20)
# calculator.multiplication(2,4)



#Approach 2
# import calmodule as cal
# cal.addition(1,2)



# # Approach 3
from calculator import *
addition(1,2)
multiplication(2,3)
