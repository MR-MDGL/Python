# Task 20
# Write a program that takes two values from the user. Check if:
#     • Both values are positive or if both values are negative.
#     • If they are mixed (one positive and one negative), print "Mixed signs".
val1=int(input("enter value 1"))
val2=int(input("enter value 2"))

if val1 > 0 and val2 > 0:
    print("positive values")
elif val1 < 0 and val2 < 0:
    print("negetive values")
else:
    print("mixed sign's ")
