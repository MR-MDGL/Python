# 6. Write a program to add 30 days to the current date and print the result in the format YYYY-MM-DD.
# print("Add 30 days:", (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d"))

import datetime as dt
toay=dt.date.today()
delayday=dt.timedelta(30)
print(f'30 days from today will be {toay + delayday} ')
#using in single line 
print("Add 30 days:", (dt.date.today() + dt.timedelta(days=30)).strftime("%Y-%m-%d"))