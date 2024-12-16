# 1. Write a Python script to create a file called example.txt, write the text "Python programming is interesting" into it, and close the file.
file=open(r'E:\BEBO-Tech\Python\pythonProject\PracticeSessions\PracticeSession20\example.txt','w')
try:
    file.write('python programming is intresting')
except Exception as e:
    print(e)