"""Five Hundred related classes
"""
from fivehundred.cards import Card, Pile, Value, PlayingCard, suits

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

class Birdie(Card):
    def __init__(self):
        Card.__init__(self, 'Birdie')

class FiveHundredDeck(Pile):
    def __init__(self, sixplayer):
        Pile.__init__(self)
        self.cards = []
        if sixplayer:
            self._six_player()
        else:
            self._four_player()
        self.shuffle()

    def _four_player(self):
        values = {
            '5' : Value('5', 'Five', 5),
            '6' : Value('6', 'Six', 6),
            '7' : Value('7', 'Seven', 7),
            '8' : Value('8', 'Eight', 8),
            '9' : Value('9', 'Nine', 9),
            '10': Value('10', 'Ten', 10),
            'J' : Value('J', 'Jack', 11),
            'Q' : Value('Q', 'Queen', 12),
            'K' : Value('K', 'King', 13),
            'A' : Value('A', 'Ace', 14),
        }
        for s in suits.values():
            for v in values.values():
                self.add(PlayingCard(s, v))
        val_four = Value('4', 'Four', 4)
        self.add(PlayingCard(suits['diamonds'], val_four))
        self.add(PlayingCard(suits['hearts'], val_four))
        self.add(Birdie())

    def _six_player(self):
        values = {
            '2' : Value('2', 'Two', 2),
            '3' : Value('3', 'Three', 3),
            '4' : Value('4', 'Four', 4),
            '5' : Value('5', 'Five', 5),
            '6' : Value('6', 'Six', 6),
            '7' : Value('7', 'Seven', 7),
            '8' : Value('8', 'Eight', 8),
            '9' : Value('9', 'Nine', 9),
            '10': Value('10', 'Ten', 10),
            '11': Value('11', 'Eleven', 11),
            '12': Value('12', 'Twelve', 12),
            #save a spot for thirteen
            'J' : Value('J', 'Jack', 14),
            'Q' : Value('Q', 'Queen', 15),
            'K' : Value('K', 'King', 16),
            'A' : Value('A', 'Ace', 17),
        }
        for s in suits.values():
            for v in values.values():
                self.add(PlayingCard(s, v))
        val_thirteen = Value('13', 'Thirteen', 13)
        self.add(PlayingCard(suits['diamonds'], val_thirteen))
        self.add(PlayingCard(suits['hearts'], val_thirteen))
        self.add(Birdie())

def valid_bid(bid):
    if bid == 'PASS':
        return True
    return bid in _BID_TABLE.keys()

def bid_value(bid):
    if not bid:
        return 0
    return _BID_TABLE.get(bid)
