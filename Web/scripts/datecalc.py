import datetime
import sys

dt  = datetime.datetime
now = dt.now()

# This gives timedelta in days
futureyear = int(sys.argv[1])
futuremonth = int(sys.argv[2])
futureday = int(sys.argv[3])

time = dt(year=(futureyear),month=(futuremonth),day=(futureday)) - dt(year=now.year, month=now.month, day=now.day)

print(time)

