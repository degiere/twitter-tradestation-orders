"""
Config file for Gmail account settings, copy .tradestation-emails.ini to ~/.tradestation-emails.ini and change
"""
__author__ = 'Chris Degiere'

from configobj import ConfigObj
from os.path import expanduser

name = '.tradestation-emails.ini'
default = expanduser("~") + "/" + name


def parse_config(file=default):
    """ parse a config file in the user's home directory for email account info """
    config = ConfigObj(file)
    if 'username' not in config or 'password' not in config or 'label' not in config:
        raise Exception("Perhaps you didn't add " + default + "? See: " + name)
    return config['username'], config['password'], config['label']


