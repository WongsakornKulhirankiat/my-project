import time
from datetime import datetime
"""value = str(time.strftime("%H%M"))
print(value)
value1 = int(value)
value1 = 1800
value2 = 1759
timeac = abs(value1 - value2)
print(timeac)"""

"""current_datetime1 = datetime.now()
current_time1 = current_datetime1.time()

current_datetime2 = datetime.now()
current_time2 = current_datetime2.time()

timeac = current_time2 - current_time1
print(timeac)"""


"""s_format = "%H:%M"
s1 = "8:00"
dt1 = datetime.strptime(s1, s_format)
s2 = "8:10"
dt2 = datetime.strptime(s2, s_format)
print(dt1,dt2)

asc =  dt1 - dt2
print(asc)
print(asc.total_seconds())
actuallytime = (asc.total_seconds() / 3600) -1
print(actuallytime)
print(round(actuallytime, 2))

if actuallytime < 0:
    print("minasu")
if actuallytime >= 0:
    print("plasu")"""


"""yearmonth = str(time.strftime("%Y%m"))
entertime = str(time.strftime("%H:%M"))

print("yearmonth:",yearmonth, "entertime:",entertime)


date = int(time.strftime("%d"))
print("date:",date, "type:",type(date))

intvalue = 100
textvalue = "{}".format(intvalue)
print("textvalue:",textvalue, "type:",type(textvalue))"""

