"""
Main runner responsible for fetching today's order emails and archiving for another processor
Schedule me to run once every 15 minutes with cron or similar
"""
__author__ = 'Chris Degiere'

from datetime import datetime, date
import pytz

from tsemail import email
from tsemail import config
from tsemail import parse

filename = 'data.txt'


def minutes_between(now, then):
    # TODO: sanity check timezone handling if deployed somewhere other than PST
    now = now.replace(tzinfo=pytz.timezone('US/Pacific'))
    return (now - then).seconds / 60


def main():
    today = date.today()
    now = datetime.now()
    print "---"
    print str(now) + " fetching order emails..."
    username, password, label = config.parse_config()
    emails = email.fetch_emails(username, password, label, today)
    print "fetched: " + str(len(emails)) + " order emails"
    for e in emails:
        print e
    email.serialize(emails, filename)
    print "wrote to: " + filename
    emails = email.deserialize(filename)
    for e in emails:
        body = e['body']
        dt = email.parse_date(e['date'])
        if parse.order(body):
            direction, quantity, symbol = parse.order_details(body)
            root, month, year = parse.contract_details(symbol)
            print "|".join([str(dt), direction, quantity, root, str(minutes_between(now, dt))])

if __name__ == "__main__":
    main()