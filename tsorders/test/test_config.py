__author__ = 'Chris Degiere'

from tsorders.config import email_config, twitter_config


def test_email_config():
    username, password, label = email_config()
    assert username
    assert password
    assert label


def test_twitter_config():
    api_key, api_secret, access_token, access_secret = twitter_config()
    assert api_key
    assert api_secret
    assert access_token
    assert access_secret
