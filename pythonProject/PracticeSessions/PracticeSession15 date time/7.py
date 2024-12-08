# calculate difference btw 10:30:00 and 14:45:30
from datetime import datetime

time1=datetime.strptime("10:30:00","%H:%M:%S")
time2=datetime.strptime("14:45:30","%H:%M:%S")
timediff= time2 - time1
print(timediff)


























#
# time1 = "10:30:00"
# time2 = "14:45:30"
#
# time_format = "%H:%M:%S"
# time_obj1 = datetime.strptime(time1, time_format)
# time_obj2 = datetime.strptime(time2, time_format)
#
# time_difference = time_obj2 - time_obj1
# total_seconds = time_difference.total_seconds()
#
# hours = int(total_seconds // 3600)
# minutes = int((total_seconds % 3600) // 60)
# seconds = int(total_seconds % 60)
#
# result = f"{hours} hours, {minutes} minutes, {seconds} seconds"
# print(result)
