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


def filter(tweet):
    created = dates.parse(tweet['created_at'])  # tweets are in utc
    text = tweet['text']
    return {'created_at': str(created), 'text': text}


def filtered(tweets):
    filtered = []
    for tweet in tweets:
        filtered.append(filter(tweet))
    return filtered


def todays_tweets(tweets):
    todays = []
    for tweet in tweets:
        if dates.is_today(dates.parse(tweet['created_at'])):
            todays.append(tweet)
    return todays





