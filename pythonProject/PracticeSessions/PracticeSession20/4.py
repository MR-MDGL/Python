# 4. Write a Python program to count the number of words in a file called document.txt.


file=open(r'E:\BEBO-Tech\Python\pythonProject\PracticeSessions\PracticeSession20\document.txt','r')
try:
    content=file.read()

except Exception as e:
    print(e)

content=content.split(' ')
print(len(content))