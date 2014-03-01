"""
Extract and archive TradeStation order emails from a Gmail account

Setup a filter in Gmail
   Matches: subject:("TradeStation - Order has been filled for ")
   Do this: Skip Inbox, Apply label "TradeStation Orders", Never send it to Spam

"""
__author__ = 'Chris Degiere'

import gmail
import json
from dateutil import parser


def fetch_emails(username, password, label, after):
    """ Fetch unread emails for today and mark read """
    g = gmail.login(username, password)
    # emails = g.mailbox(label).mail(unread=True, after=after)
    emails = g.mailbox(label).mail(after=after)
    text = []
    for e in emails:
        e.fetch()
        id = e.headers['Message-ID']
        date = e.headers['Date']  # 'Thu, 27 Feb 2014 11:29:01 -0800 (PST)'
        body = e.body
        text.append({'id': id, 'date': date, 'body': body})
    g.logout()
    return text


def serialize(emails, filename):
    """ dump json representation of relevent email parts to file """
    data = json.dumps(emails, sort_keys=True, indent=4, separators=(',', ': '))
    f = open(filename, 'w')
    f.write(data)
    f.close()


def deserialize(file):
    """ read data file and parser json back to array of dicts """
    with open(file, 'r') as f:
        data = f.read()
    return json.loads(data)


def parse_date(str):
    """ parse gmail time stamp: Fri, 28 Feb 2014 08:00:01 -0800 (PST) """
    return parser.parse(str)
