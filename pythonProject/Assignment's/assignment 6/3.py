# 3.Write a program to print the current date and time in the format YYYY-MM-DD HH:MM:SS. Create a
# datetime object for 1st January 2025,

import datetime as dt
print(dt.datetime.now())
future_date = dt.datetime(2025, 1, 1)
print(future_date.date())
