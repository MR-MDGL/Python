'''
Hi, my name is Sunil Mudgil, and I am from Bhiwani, Haryana. I am currently in the third semester of my MCA program and
have completed my BCA degree from Chaudhary Bansi Lal University, Bhiwani.
Presently, I am learning software testing at Bebo Technologies, where I am improving my skills and gaining
practical knowledge. I am a dedicated team player, passionate about my work,
and committed to continuously expanding my expertise.
I am particularly interested in securing a role as a Software Tester at Bebo Technologies to gain hands-on
industry experience and further enhance my skills in the field.
'''




import datetime
# print(datetime.timedelta)
print(datetime.timezone)






print('-----------------------------------------------')
curr_datetime=datetime.datetime.now()
print(f'current date and time is {curr_datetime}')

print()
print()
print('-----------------------------------------------')
date=datetime.date(2024,12,6)
print('today is ',date)
time=datetime.time(11,22,30)
print(time)
print()
print()
print('----------------------------print differtly-------------------')
now=datetime.datetime.now()
print('year',now.year)
print('moth',now.month)
print('day',now.day)
print(now.minute)
print(now.second)
print()
print()
print()
print()
print()
print('-----------------------------------------------')
today=datetime.date.today()
future_date=today+datetime.timedelta(days=10)
past_date=today-datetime.timedelta(days=10)

print(f'10 days after today will be {future_date}')
print(f'10 days befor today was {past_date}')

