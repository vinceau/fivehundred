

_BID_TABLE = {
    '6S': 40,
    '6C': 60,
    '6D': 80,
    '6H': 100,
    '6X': 120,
    '7S': 140,
    '7C': 160,
    '7D': 180,
    '7H': 200,
    '7X': 220,
    '8S': 240,
    '8C': 260,
    '8D': 280,
    '8H': 300,
    '8X': 320,
    '9S': 340,
    '9C': 360,
    '9D': 380,
    '9H': 400,
    '9X': 420,
    '10S': 440,
    '10C': 460,
    '10D': 480,
    '10H': 500,
    '10X': 520,
    'M': 250,
    'OM': 500,
    #leave out blind misere for now
    #'BM': 1000,
}

def valid_bid(bid):
    if bid == 'PASS':
        return True
    return bid in _BID_TABLE.keys()

def bid_value(bid):
    if not bid:
        return 0
    return _BID_TABLE.get(bid)

class Bid(object):
    def __init__(self, identifier):
        self.identifier = identifier
        self.suit = self._get_suit(identifier)
        self.worth = bid_value(identifier)
        self.tricks_needed = 0 #misere
        num = ''.join(filter(str.isdigit, identifier))
        if num:
            self.tricks_needed = int(num)


    def __lt__(self, other):
        return self.worth < other.worth

    def _get_suit(self, identifier):
        last = identifier[-1]
        if last == 'M' or  last == 'X':
            return 'notrumps'
        if last == 'D':
            return 'diamonds'
        if last == 'C':
            return 'clubs'
        if last == 'H':
            return 'hearts'
        if last == 'S':
            return 'spades'
