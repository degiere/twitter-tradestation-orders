"""
Main runner responsible for fetching today's order emails and archiving for another processor
Schedule me to run once every 15 minutes with cron or similar
"""
__author__ = 'Chris Degiere'

from tsemail import email
from tsemail import config

import datetime

filename = 'data.txt'


def main():
    today = datetime.date.today()
    print "---"
    print str(datetime.datetime.now()) + " fetching order emails..."
    username, password, label = config.parse_config()
    emails = email.fetch_emails(username, password, label, today)
    print "fetched: " + str(len(emails)) + " order emails"
    for e in emails:
        print e
    email.serialize(emails, filename)
    print "wrote to: " + filename


if __name__ == "__main__":
    main()