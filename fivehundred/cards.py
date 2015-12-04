#!/usr/bin/python
from random import shuffle

class Card(object):
    def __init__(self, identifier, name=None):
        self.identifier = identifier
        self.name = name

    def __str__(self):
        return self.name if self.name else self.identifier

class Pile(object):

    def __init__(self):
        self.cards = []

    def __iter__(self):
        return iter(self.cards)

    def get(self, identifier):
        """Returns a specific card from the pile 
        """
        for i in range(len(self.cards)):
            if self.cards[i].identifier == identifier:
                card = self.cards[i]
                del self.cards[i]
                return card
        return None

    def get_top(self):
        """Returns the card on the top of the pile
        """
        return self.cards.pop()

    def shuffle(self):
        """
        shuffle the cards
        """
        shuffle(self.cards)

    def show(self):
        #print it in reverse (first one printed is top of pile)
        for c in reversed(self.cards):
            print(c)

    def add(self, card):
        """Adds a card to the top of the pile (will be drawn next)
        """
        self.cards.append(card)

    def extend(self, pile):
        """Adds multiple cards to pile in the given order
        """
        self.cards.extend(pile)
        pile.empty()

    def size(self):
        return len(self.cards)

    def empty(self):
        self.cards = []

    def deal(self, players, num):
        """Deals num cards to each player in players
        """
        for _ in range(num):
            for p in players:
                p.draw(self)
                if self.size() == 0:
                    return

class Suit(object):
    def __init__(self, identifier, name, rank):
        self.identifier = identifier
        self.name = name
        self.rank = rank

#in a normal deck (e.g. poker) suits are all ranked the same
suits = {
    'diamonds' : Suit('D', 'Diamonds', 1),
    'clubs' : Suit('C', 'Clubs', 1),
    'hearts' : Suit('H', 'Hearts', 1),
    'spades' : Suit('S', 'Spades', 1),
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

    def __lt__(self, other):
        return self.get_rank() < other.get_rank()

    def __eq__(self, other):
        return self.get_rank() == other.get_rank()

    def get_rank(self):
        """Calculated value taking into account suit and rank
        """
        return self.suit.rank * 1000 + self.value.rank

class StandardDeck(Pile):
    def __init__(self):
        Pile.__init__(self)
        self.cards = []
        #dictionary value ordering is not preserved!!
        for s in suits.values():
            for v in values.values():
                self.add(PlayingCard(s, v))
        self.shuffle()

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = Pile()

    def draw(self, pile, num=1):
        """Given a pile, the player draws num cards from the top of the pile.
        """
        for _ in range(num):
            self.hand.add(pile.get_top())

    def add(self, card):
        """Given a card, the player adds it to their hand.
        """
        self.hand.add(card)

    def take(self, pile):
        """Given a pile, the player takes it and ands the whole pile to their
        hand.
        """
        for card in pile:
            self.add(card)
        pile.empty()


if __name__ == '__main__':
    p1 = Player('Player 1')
    p2 = Player('Player 2')
    players = [p1, p2]
    deck = StandardDeck()
    #deal 5 cards to each player
    deck.deal(players, 5)
