# 5. Read a CSV file named data.csv and print its contents line by line.
file=open(r'E:\BEBO-Tech\Python\pythonProject\PracticeSessions\PracticeSession20\csvfile.csv','w')
try:
    file.write('line1 ')
    file.write('line2\n')
    file.write('line3\n')
    file.write('line4\n')
except Exception as e:
    print(e)
file.close()

file=open(r'E:\BEBO-Tech\Python\pythonProject\PracticeSessions\PracticeSession20\csvfile.csv','r')
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())