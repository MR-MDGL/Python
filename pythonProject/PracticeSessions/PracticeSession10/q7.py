# Create a function to check whether a given string is a palindrome.
str=input("enter your string ")
def pallindrome(str):
    bk=str
    rev=""
    for i in str:
        rev=i+rev
    # print(rev,bk)

    if rev == bk:
        return True
    else:
        return False

print(pallindrome(str))
