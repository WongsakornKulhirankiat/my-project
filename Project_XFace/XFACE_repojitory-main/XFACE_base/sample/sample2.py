import time
from datetime import datetime

import sample2_2

# start time
starttime = time.time()

t1 = "8:00"
t2 = "17:00"
"""dt1 = datetime.strptime(t1, "%H:%M")
dt2 = datetime.strptime(t2, "%H:%M")
caluculate = dt2 - dt1
workingtime = round((caluculate.total_seconds() / 3600), 2)
print(workingtime)"""

sample2_2.caluculate_method(t1,t2)

# end time
endtime = time.time()

# Elpased time
elpased_time = endtime-starttime
#print("elpased_time no module:",elpased_time)
print("elpased_time module:",elpased_time)