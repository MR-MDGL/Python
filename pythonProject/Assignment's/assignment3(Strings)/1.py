# 1.Check if a string is a palindrome.
n = input("enter string ")
rev_str = ""
for i in n:
    rev_str = i + rev_str

if rev_str == n:
    print("palindrome")
else:
    print("not palindrome")
