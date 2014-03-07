"""
Main runner responsible for fetching today's order emails and archiving for another processor
Schedule me to run once every 15 minutes with cron or similar
"""
__author__ = 'Chris Degiere'

from tsorders import dates
from tsorders import config
from tsorders import email
from tsorders import parse
from tsorders import io
from tsorders import twtr

email_file = 'emails.txt'
tweet_file = 'tweets.txt'


def main():
    print "---"
    now = dates.now_tz()

    print str(now) + " fetching order emails..."
    username, password, label = config.email_config()
    emails = email.fetch_emails(username, password, label, dates.today())

    print "fetched: " + str(len(emails)) + " order emails"
    for e in emails:
        print e

    io.serialize(emails, email_file)
    print "wrote to: " + email_file

    emails = io.deserialize(email_file)
    for e in emails:
        body = e['body']
        dt = dates.parse(e['date'])
        if parse.order(body):
            direction, quantity, symbol = parse.order_details(body)
            root, month, year = parse.contract_details(symbol)
            print "|".join([str(dt), direction, quantity, root, str(dates.minutes_between(now, dt))])

    print "fetching tweets..."
    api_key, api_secret, access_token, access_secret = config.twitter_config()
    api = twtr.login(api_key, api_secret, access_token, access_secret)
    tweets = twtr.filtered(twtr.latest(api))

    io.serialize(tweets, tweet_file)
    print "wrote tweets to: " + tweet_file

    tweets = twtr.todays_tweets(tweets)
    for tweet in tweets:
        print str(tweet['created_at']) + "|" + tweet['text']


if __name__ == "__main__":
    main()