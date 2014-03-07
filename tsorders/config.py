"""
Set these environment variables:
    # for email access
    export TSEMAIL_USERNAME='yourusername'
    export TSEMAIL_PASSWORD'='abcdefghijklmnop'
    export TSEMAIL_LABEL='Your Label'
    # for twitter access
    export TSTWITTER_API_KEY='abcd1234abcd1234'
    export TSTWITTER_API_SECRET'='abcd1234abcd1234abcd1234abcd1234'
    export TSTWITTER_ACCESS_TOKEN='abcd1234abcd1234abcd1234abcd1234'
    export TSTWITTER_ACCESS_SECRET='abcd1234abcd1234abcd1234abcd1234'
"""
__author__ = 'Chris Degiere'

import os


def missing(envs):
    for env in envs:
        if env not in os.environ:
            raise Exception("Perhaps you didn't set these environment variables? " + ", ".join(envs))


def email_config():
    """ get email config values from environment variables or alert """
    envs = ['TSEMAIL_USERNAME', 'TSEMAIL_PASSWORD', 'TSEMAIL_LABEL']
    missing(envs)
    return os.environ['TSEMAIL_USERNAME'], os.environ['TSEMAIL_PASSWORD'], os.environ['TSEMAIL_LABEL']


def twitter_config():
    """ get twitter config values from environment variables or alert """
    envs = ['TSTWITTER_API_KEY', 'TSTWITTER_API_SECRET', 'TSTWITTER_ACCESS_TOKEN', 'TSTWITTER_ACCESS_SECRET']
    missing(envs)
    api_key = os.environ['TSTWITTER_API_KEY']
    api_secret = os.environ['TSTWITTER_API_SECRET']
    access_token = os.environ['TSTWITTER_ACCESS_TOKEN']
    access_secret = os.environ['TSTWITTER_ACCESS_SECRET']
    return api_key, api_secret, access_token, access_secret
