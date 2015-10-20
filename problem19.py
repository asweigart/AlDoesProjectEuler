import datetime
import logging
logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.CRITICAL)

oneDay = datetime.timedelta(days=1)

dt = datetime.datetime(1901, 1, 1, 0, 0, 0)
lastDay = datetime.datetime(2000, 12, 31, 0, 0 ,0)

sundays = 0
while dt < lastDay:
    logging.debug('%s  %s  %s' % (dt, dt.day, dt.weekday()))
    if dt.day == 1 and dt.weekday() == 6:
        sundays += 1

    dt += oneDay
print(sundays)