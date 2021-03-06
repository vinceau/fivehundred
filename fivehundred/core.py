"""Five Hundred related classes
"""
from .cards import Card, Pile, Value, PlayingCard, suits

class Birdie(Card):
    def __init__(self):
        Card.__init__(self, 'Birdie')

class FiveHundredDeck(Pile):
    def __init__(self, sixplayer):
        Pile.__init__(self)
        self.cards = []
        self._four_player()
        if sixplayer:
            self._six_player()
        self.shuffle()
        assert self.size() == (63 if sixplayer else 43)

    def _four_player(self):
        values = {
            '5' : Value('5', 'Five', 5),
            '6' : Value('6', 'Six', 6),
            '7' : Value('7', 'Seven', 7),
            '8' : Value('8', 'Eight', 8),
            '9' : Value('9', 'Nine', 9),
            '10': Value('10', 'Ten', 10),
            'J' : Value('J', 'Jack', 14),
            'Q' : Value('Q', 'Queen', 15),
            'K' : Value('K', 'King', 16),
            'A' : Value('A', 'Ace', 17),
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
            '11': Value('11', 'Eleven', 11),
            '12': Value('12', 'Twelve', 12),
        }
        for s in suits.values():
            for v in values.values():
                self.add(PlayingCard(s, v))
        val_thirteen = Value('13', 'Thirteen', 13)
        self.add(PlayingCard(suits['diamonds'], val_thirteen))
        self.add(PlayingCard(suits['hearts'], val_thirteen))
        val_four = Value('4', 'Four', 4)
        self.add(PlayingCard(suits['spades'], val_four))
        self.add(PlayingCard(suits['clubs'], val_four))
