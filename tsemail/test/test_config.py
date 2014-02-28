__author__ = 'Chris Degiere'

from tsemail.config import parse_config


def test_parse_config():
    username, password, label = parse_config('.tradestation-emails.ini')
    assert username == "yourusername"
    assert password == "abcdefghijklmnop"
    assert label == "Your Label"
