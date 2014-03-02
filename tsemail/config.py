"""
Set these environment variables:
    export TSEMAIL_USERNAME='yourusername'
    export TSEMAIL_PASSWORD'='abcdefghijklmnop'
    export TSEMAIL_LABEL='Your Label'
"""
__author__ = 'Chris Degiere'

import os

envs = ['TSEMAIL_USERNAME', 'TSEMAIL_PASSWORD', 'TSEMAIL_LABEL']


def config():
    """ get config values from environment variables or alert """
    for env in envs:
        if env not in os.environ:
            raise Exception("Perhaps you didn't set these environment variables? " + ", ".join(envs))
    return os.environ['TSEMAIL_USERNAME'], os.environ['TSEMAIL_PASSWORD'], os.environ['TSEMAIL_LABEL']


