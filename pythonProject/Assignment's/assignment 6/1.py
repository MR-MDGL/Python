# Calculate the difference in days between two dates: 15th August 2025 and 1st January 2025.
import datetime as dt
fromdt=dt.date(2025,1,1)
todt=dt.date(2025,8,15)
diff=todt - fromdt
print(diff.days)

