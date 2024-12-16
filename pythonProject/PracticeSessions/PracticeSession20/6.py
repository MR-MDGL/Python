# 6. Write a program to copy the contents of a file source,txt to another file destination.txt.
file=open(r'E:\BEBO-Tech\Python\pythonProject\PracticeSessions\PracticeSession20\document.txt','r')
try:
    content=file.read()
except Exception as e:
    print(e)

file.close()
file2=open(r'E:\BEBO-Tech\Python\pythonProject\PracticeSessions\PracticeSession20\q6writefile.txt','w')
try:
    file2.write(content)
except Exception as e:
    print(e)


