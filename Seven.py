# date handling

# date = "26-08-2023"
# print(type(date))

# importing date module (module ye hote hain ke kisi bande ne koi kaam kiya hai or hum use use karte hain)
# (built-in modules wo hote hain jinhen use karne ke liye koi extra installation ki zaroorat nahi hoti hai example: json, os, sys, base64, datetime)

# import datetime

# from datetime import datetime
# from datetime import time
# from datetime import date
# from datetime import datetime, date, time

# current_date = date.today()
# print(current_date)

# current_date_time = datetime.now()
# print(current_date_time)

# print(current_date.year)
# print(current_date.month)
# print(current_date.day)


# # create date time from integer or from string

# my_day = 26
# my_month = 8
# my_year = 2023


# d = date(year=my_year, day=my_day, month=my_month)
# print(d)

# # Create date from string which are  in the iso format
# # (ISO Format)
# date_today = "2023-08-26" 
# date_today = datetime.fromisoformat(date_today)
# print(date_today)
# # Create date from string which are not in the iso format

# invalid_date = "26-08-2023"

# valid_date = datetime.strptime(invalid_date, "%d-%m-%Y")
# print(valid_date)

# datetime object banate hi isi liye hain taake hum datetime ko manipulate karsaken
# dt = datetime.now()
# string_date = str(dt)

# iso_date = datetime.strptime(string_date , "%Y-%m-%d %H:%M:%S.%f")
# print(iso_date)

# dt = "2023-01-01 23:59:59"
# dt_object = datetime.fromisoformat(dt)

# x = dt_object.replace(year=2000, month = 5, day = 12)
# print(x)

# from dateutil import parser

# dt = "26-03-02"
# date_object = parser.parse(dt)
# print(date_object)

# date time manipulation using time delta

from datetime import timedelta

# dt = date.today()

# two_days_back = dt - timedelta(days=2)
# print(two_days_back)

# x = date.fromisoformat("2023-08-12")

# for i in range(1, 10):
#     # change_dt = x + timedelta(days=i)
#     change_dt = x.replace(day = (x.day + i))
#     print(change_dt)

# # calculate difference between dates

# curren_time = datetime.now()
# custom_date = datetime.now()

# custom_date = custom_date.replace(day=2)
# print(custom_date)
# print(curren_time)

# diff = curren_time - custom_date
# print(diff)

# # relative delta khud se parhna hai

# from dateutil.relativedelta import relativedelta

# date_today = date.today()

# Change_date = date_today - relativedelta(month = 2)
# print(Change_date)

# import calendar
# kisi bhi month ki last date dehkne ke liye ke wo month 30 ka hai ya 31 ka
# month = calendar.monthrange(2023, 12) 
# print(month)

# import pytz

# current_date = datetime.now(tz = pytz.timezone("Asia/Karachi"))
# print(current_date)