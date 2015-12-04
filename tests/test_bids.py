from fivehundred.bids import valid_bid, bid_value, Bid

def test_valid_bids():
    assert valid_bid('OM')
    assert valid_bid('6H')
    assert valid_bid('10C')
    assert not valid_bid('asdf')
    assert not valid_bid('19C')

def test_bid_values():
    b = Bid('6C')
    assert b.suit == 'clubs'
    assert b.tricks_needed == 6
    assert b.worth == 60
    b = Bid('OM')
    assert b.suit == 'notrumps'
    assert b.tricks_needed == 0 #must win 0 tricks
    assert b.worth == 500
    b = Bid('7X')
    assert b.suit == 'notrumps'
    assert b.tricks_needed == 7 #must win 0 tricks
    assert b.worth == 220
