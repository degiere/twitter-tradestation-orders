"""
Main runner responsible for fetching today's order emails and archiving for another processor
Schedule me to run once every 15 minutes with cron or similar
"""
__author__ = 'Chris Degiere'

from tsorders import dates
from tsorders import config
from tsorders import email
from tsorders import text
from tsorders import io
from tsorders import twtr

email_file = 'emails.txt'
tweet_file = 'tweets.txt'
delay_minutes = 30


def main():
    print "---"
    now = dates.now_tz()

    print str(now) + " fetching order emails..."
    username, password, label = config.email_config()
    emails = email.fetch_emails(username, password, label, dates.today())

    print "fetched: " + str(len(emails)) + " order emails"
    # for e in emails:
    #     print e

    io.serialize(emails, email_file)
    print "wrote to: " + email_file

    emails = io.deserialize(email_file)  # these must be sorted by oldest to newest
    positions = {}
    for e in emails:
        body = e['body']
        dt = dates.parse(e['date'])
        if text.order(body):
            type, quantity, symbol = text.order_details(body)
            root, month, year = text.contract_details(symbol)
            if root not in positions:
                positions[root] = text.as_direction(type).lower()
            # print "|".join([str(dt), direction, quantity, root, str(dates.minutes_between(now, dt))])
    print positions

    print "fetching tweets..."
    api_key, api_secret, access_token, access_secret = config.twitter_config()
    api = twtr.login(api_key, api_secret, access_token, access_secret)
    tweets = twtr.filtered(twtr.latest(api))

    io.serialize(tweets, tweet_file)
    print "wrote tweets to: " + tweet_file

    print "checking positions against delay and against tweets:"
    # check today's tweets and remove from position if already posted or newer than 30 minutes
    tweets = twtr.todays_tweets(tweets)
    for tweet in tweets:
        stamp = tweet['created_at']
        body = tweet['text']
        print str(stamp) + "|" + body
        mins = dates.minutes_between(now, dates.parse(stamp))
        print "Message is: " + str(mins) + " minutes old"
        # only post if at least 30 minutes old
        root, direction = text.position(tweet['text'])
        if root in positions:
            print "   already posted tweet for: " + direction.capitalize() + " " + root
            del positions[root]

    # only post one per cycle
    if positions:
        symbol = positions.keys().pop()
        direction = positions[symbol]
        print "composing tweet for: " + direction.capitalize() + " " + symbol
        tweet = text.compose(symbol, direction)
        print tweet
        print "posting..."
        #twtr.post(tweet, api)


if __name__ == "__main__":
    main()