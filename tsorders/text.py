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

mapping = {
    'NG': {'name': 'Natural Gas', 'link': 'http://bit.ly/MEZwMR'},
    'GC': {'name': 'Gold', 'link': 'http://bit.ly/1mTWmlO'},
    'CL': {'name': 'Crude Oil', 'link': 'http://bit.ly/1jCKLUj'}
}


def as_tag(s):
    pattern = re.compile(r'\s+')
    s = re.sub(pattern, '', s)
    return "#" + s.lower()


def by_tags(m):
    return {as_tag(m[root]['name']): root for root in m.keys()}


tag_root = by_tags(mapping)

default_tags = ['daytrading', 'commodities', 'futures', 'tradingsystems']


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


def as_direction(type):
    if type == 'Sell':
        return 'Short'
    if type == 'Buy':
        return 'Long'


def direction(s):
    s = s.lower()
    m = re.search('.*\s+(long|short)\s+.*', s)
    if m and m.group(1):
        return m.group(1)


def mapping_tags():
    return [as_tag(mapping[v]['name']) for v in mapping.keys()]


def position(s):
    s = s.lower()
    m = re.search('.*\s+(long|short)\s+.*(' + '|'.join(mapping_tags()) + ').*', s)
    if m and m.group(1) and m.group(2):
        return tag_root[m.group(2)], m.group(1)
    return None, None


def compose(symbol, direction):
    s = "New " + direction.lower() + " position in " + mapping[symbol]['name'] + " futures today: "
    s = s + mapping[symbol]['link'] + " " + " ".join([as_tag(t) for t in default_tags])
    s = s + " " + as_tag(mapping[symbol]['name'])
    return s


def one_line(s):
    return s.replace('\t', ' ').replace('\n', '\ ').replace('\r', ' ')