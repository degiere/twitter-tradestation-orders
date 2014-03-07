"""
Extract and archive TradeStation order emails from a Gmail account

Setup a filter in Gmail
   Matches: subject:("TradeStation - Order has been filled for ")
   Do this: Skip Inbox, Apply label "TradeStation Orders", Never send it to Spam

"""
__author__ = 'Chris Degiere'

import gmail


def fetch_emails(username, password, label, after):
    """ Fetch unread emails for today and mark read """
    g = gmail.login(username, password)
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
