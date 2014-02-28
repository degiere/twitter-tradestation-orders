"""
Parse details from TradeStation TradeManager order emails
"""
__author__ = 'Chris Degiere'

import re

# Jan (F), Feb (G), Mar (H)
# Apr (J), May (K), Jun (M)
# Jul (N), Aug (Q), Sep (U)
# Oct (V), Nov (X), Dec (Z)
months = ['F', 'G', 'H', 'J', 'K', 'M', 'N', 'Q', 'U', 'V', 'X', 'Z']


def order(body):
    """ Is order email? """
    m = re.search('TradeStation - Order has been filled for', body)
    if m and m.group(0):
        return True


def order_details(body):
    """ Extract the direction, quantity, and symbol """
    m = re.search('.*Order:\s+(Buy|Sell)\s+(\d+)\s+(\w+)\s+@.*', body)
    if m and m.group(1) and m.group(2) and m.group(3):
        return m.group(1), m.group(2), m.group(3)


def contract_details(symbol):
    """ Extract symbol root, month, and year if futures symbol """
    m = re.search('^([A-Z][A-Z])(' + '|'.join(months) + ')(\d\d)$', symbol)
    if m and m.group(1) and m.group(2) and m.group(3):
        return m.group(1), m.group(2), m.group(3)
