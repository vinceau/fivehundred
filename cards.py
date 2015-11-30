#!/usr/bin/python
from random import shuffle

class Card(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Pile(object):

    def __init__(self):
        self.cards = []

    def draw(self):
        """
        draw a card
        """
        return self.cards.pop()

    def shuffle(self):
        """
        shuffle the cards
        """
        shuffle(self.cards)

    def show(self):
        for c in self.cards:
            print(c)

    def add(self, card):
        self.cards.append(card)

    def size(self):
        return len(self.cards)

class Suit(object):
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

#in a normal deck (e.g. poker) suits are all ranked the same
suits = {
    'diamonds' : Suit('Diamonds', 1),
    'clubs' : Suit('Clubs', 1),
    'hearts' : Suit('Hearts', 1),
    'spades' : Suit('Spades', 1),
}

class Value(object):
    def __init__(self, identifier, name, rank):
        self.identifier = identifier
        self.name = name
        self.rank = rank

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
    'J' : Value('J', 'Jack', 11),
    'Q' : Value('Q', 'Queen', 12),
    'K' : Value('K', 'King', 13),
    'A' : Value('A', 'Ace', 14),
}

class PlayingCard(Card):
    def __init__(self, suit, value):
        Card.__init__(self, value.name + ' of ' + suit.name)
        self.suit = suit
        self.value = value
        self.rank = suit.rank * 100 + value.rank

class StandardDeck(Pile):
    def __init__(self):
        Pile.__init__(self)
        self.cards = []
        #dictionary value ordering is not preserved!!
        for s in suits.values():
            for v in values.values():
                self.add(PlayingCard(s, v))
        self.shuffle()

