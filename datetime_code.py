# Always represent time in UTC and do conversions to local time as the final step
# before presentation
from datetime import datetime, timezone
from time import mktime
import pytz


def get_utc_from_present_localtime():
    now = datetime(2018, 3, 8, 13,24,11)
    now_utc = now.replace(tzinfo=timezone.utc)
    now_local = now_utc.astimezone()
    print (now_local)

def get_unix_timestamp_from_localtime():
    time_str = '2018-3-8 13:24:11'
    now = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
    time_tuple = now.timetuple()
    utc_now = mktime(time_tuple)
    print (utc_now)

def get_utc_from_other_timezone():
    arrival_nyc = '2018-3-8 13:24:11'
    nyc_dt_naive = datetime.strptime(arrival_nyc, '%Y-%m-%d %H:%M:%S')
    eastern = pytz.timezone('US/Eastern')
    nyc_dt = eastern.localize(nyc_dt_naive)
    utc_dt = pytz.utc.normalize(nyc_dt.astimezone())
    print (nyc_dt)
    print (utc_dt)
    pacific = pytz.timezone('US/Pacific')
    sf_dt = pacific.normalize(utc_dt.astimezone(pacific))
    print (sf_dt)

if __name__ == '__main__':
    #get_utc_from_present_localtime()
    #get_unix_timestamp_from_localtime()
    get_utc_from_other_timezone()