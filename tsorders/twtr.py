"""
Authorize, read last tweets for user, post tweets using twitter
https://pypi.python.org/pypi/twitter/1.13.1
"""
__author__ = 'Chris Degiere'

import twitter

from tsorders import dates


def login(api_key, api_secret, access_token, access_secret):
    auth = twitter.oauth.OAuth(access_token, access_secret, api_key, api_secret)
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api


def latest(api):
    return api.statuses.user_timeline(count=10)  # defaults to authorized user


def post(message, api):
    api.statuses.update(status=message)


def filter(tweet):
    created = dates.parse(tweet['created_at'])  # tweets are in utc
    text = tweet['text']
    return {'created_at': str(created), 'text': text}


def filtered(tweets):
    return [filter(tweet) for tweet in tweets]


def todays_tweets(tweets):
    return [tweet for tweet in tweets if dates.is_today(dates.parse(tweet['created_at']))]
