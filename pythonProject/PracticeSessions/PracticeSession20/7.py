# 7. Write a script that takes a file name as input and prints the number of lines, words, and characters in the file.
# file_name=input('enter the name of ur file')


# file=open(fr'E:\BEBO-Tech\Python\pythonProject\PracticeSessions\PracticeSession20\{file_name}.txt','r')
file=open(r'E:\BEBO-Tech\Python\pythonProject\PracticeSessions\PracticeSession20\readfile.txt','r')

content=file.read()

lines=content.count('\n')+1
print(lines)

words=len(content.split(" "))
print(words)

char = len(content)
print(char)








