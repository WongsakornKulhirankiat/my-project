import time
from datetime import datetime

def caluculate_method(t1,t2):
    dt1 = datetime.strptime(t1, "%H:%M")
    dt2 = datetime.strptime(t2, "%H:%M")
    caluculate = dt2 - dt1
    workingtime = round((caluculate.total_seconds() / 3600), 2)
    print(workingtime)


t11 = 0.008708715438842773   #elpased_time no module: 
t22 = 0.008172273635864258   #elpased_time module: 

time_difference = t11 - t22
print(round(time_difference,5))  # -> 0.00054