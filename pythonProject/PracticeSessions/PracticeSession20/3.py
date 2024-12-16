# 3. Modify a file named log.txt by appending the current date and time at the end of the file.
import datetime as dt

file=open(r'E:\BEBO-Tech\Python\pythonProject\PracticeSessions\PracticeSession20\example.txt','a')
try:
    file.write('\n')
    file.write(str(dt.datetime.now()))
except Exception as e:
    print(e)