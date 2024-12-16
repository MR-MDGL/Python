# 8. Write a program to merge the contents of two files, filel.txt and file2.txt, into a new file called merged.txt.
file=open(r'E:\BEBO-Tech\Python\pythonProject\PracticeSessions\PracticeSession20\document.txt','r')
try:
    content1=file.read()
except Exception as e:
    print(e)

file.close()
file2=open(r'E:\BEBO-Tech\Python\pythonProject\PracticeSessions\PracticeSession20\q6writefile.txt','r')
try:
    content2=file2.read()
except Exception as e:
    print(e)
file3=open(r'E:\BEBO-Tech\Python\pythonProject\PracticeSessions\PracticeSession20\q8_finalfileappend.txt','w')
try:
    file3.write(content1)
    file3.write(content2)
except Exception as e:
    print(e)
