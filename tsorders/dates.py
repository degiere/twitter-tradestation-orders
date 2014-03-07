__author__ = 'Chris Degiere'

from dateutil import parser
from datetime import datetime
import pytz

# standardize all dates to EST for correct day boundaries related to market hours
tz = pytz.timezone('US/Eastern')


def today():
    return now_tz().date()


def is_today(d):
    now = now_tz()
    return d.year == now.year and d.month == now.month and d.day == now.day


def now_tz():
    return datetime.now(tz)


def parse(s):
    return parser.parse(s).astimezone(tz)


def minutes_between(now, then):
    return (now - then).seconds / 60

