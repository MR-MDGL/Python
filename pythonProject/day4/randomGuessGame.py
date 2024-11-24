# #game that has a random value and we have to guess the number if num==guess print "guessed" in count and the real number is "R"
# import random
# r=random.randint(1,100)
# print(r)
# guessed=False
# count=0
# while guessed==False:
#     guess=int(input("enter value"))
#     if(guess>r):
#         print("number guessed is lower")
#         count+=1
#     elif(guess<r):
#         print("number is higher")
#         count+=1
#
#     elif(guess==r):
#         print(f"you guessed in {count} times and the number is {r}")
#         guessed=True
import random
r=random.randint(1,100)
print(r)
guessed=False
count=1
while guessed==False:
    guess=int(input("enter your guess"))
    if guess > r:
        print("number is lower")
        count+=1
    elif(guess<r):
        print("num is highter")
        count+=1
    elif guess ==r:
        print(f"guess it in {count} times")
    guess= True