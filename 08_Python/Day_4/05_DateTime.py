# import datetime
# print(dir(datetime))



from datetime import datetime
import pytz
# now = datetime.now()
     #"OR"
# now = datetime(2026,6,9)
# now.strtime()
now = datetime.now(pytz.timezone('US/Eastern'))
day = now.day
month = now.month
year = now.year
hr = now.hour
minute = now.minute
second = now.second
print(day, month, year, hr, minute, second,now)
print(f'day={day}/Month={month}/Year={year}/Hour={hr}/minute={minute}/second={second}')