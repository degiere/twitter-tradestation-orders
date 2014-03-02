__author__ = 'Chris Degiere'

from tsemail.config import config


def test_config():
    username, password, label = config()
    assert username
    assert password
    assert label
