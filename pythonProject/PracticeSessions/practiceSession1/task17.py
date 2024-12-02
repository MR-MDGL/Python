# Task 17
#
# Write a program that checks if a student is eligible for admission to a specific course. The criteria for eligibility are:
#     • The student must have scored at least 80% in math and 70% in science.
#     • Or they must have a total average score of at least 75%.

maths=int(input("enter math's marks out of  100"))
sci=int(input("enter science marks out of 100"))

if maths>=80 and sci>=70:
    if ((maths+sci)/2)>=75:
        print("you are eligible for admission ")
    else:
        print("you are not eligible for admission ")
else:
    print("you are not eligible ")
