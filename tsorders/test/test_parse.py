__author__ = 'Chris Degiere'

from tsorders.text import *

ex1 = """TradeStation - Order has been filled for NGJ14
    Order: Sell 1 NGJ14 @ Market
    Qty Filled: 1
    Filled Price: 4.5670
    Duration: Day
    Route: N/A
    Account: 12345678
    Order#: 1-2345-6789"""

ex2 = """TradeStation - Order has been filled for NGJ14
    Order: Buy 2 GCG14 @ Market
    Qty Filled: 2
    Filled Price: 1331.80
    Duration: Day
    Route: N/A
    Account: 12345678
    Order#: 1-2345-6789"""

ex3 = """Your TradeStation add-on has been ordered
    Here's the details...
    SKU12345 $59.95
    Trades @ES"""


def test_order():
    assert order(ex1)
    assert order(ex2)
    assert not order(ex3)


def test_order_details():
    assert order_details(ex1) == ('Sell', '1', 'NGJ14')
    assert order_details(ex2) == ('Buy', '2', 'GCG14')
    assert not order_details(ex3)


def test_contract_details():
    assert contract_details('NGJ14') == ('NG', 'J', '14')
    assert not contract_details('NGJ2014')
    assert not contract_details('NGA14')
    assert not contract_details('@GC')
    assert not contract_details('AAPL')