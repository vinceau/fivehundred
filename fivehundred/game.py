"""The game handler
"""
from .core import FiveHundredDeck
from .bids import valid_bid, Bid
from .cards import Player, Pile

class NotEnoughPlayersException(Exception):
    def __init__(self):
        Exception.__init__(
            self,
            "You need either 4 or 6 players for a game of 500."
        )

class SamePlayerNameException(Exception):
    def __init__(self):
        Exception.__init__(
            self,
            "Players need to have different names."
        )

class Order(object):
    """Keeps track of the order, who has delt etc.
    """
    def __init__(self, players, start=0):
        self.players = players
        self.start = start #this person starts

    def __iter__(self):
        i = 0
        no_players = len(self.players)
        while i < no_players:
            turn = i + self.start
            yield self.players[turn % no_players]
            i += 1

    def next_starter(self):
        """The next person in line starts
        """
        self.start += 1


class Round(object):
    """This will manage the round. Shuffle the deck, handle the bidding, handle
    the play, and utlimately return when the 10 tricks are over with the
    winning team and the amount of points earned or lost.
    """
    def __init__(self, players, dealer=0):
        self.players = players
        #mapping from player names to player objects
        self.player_map = {}
        for p in players:
            self.player_map[p] = Player(p)
        self.kitty = Pile()
        self.state = 'initialised'
        self.turn = None #who's turn is it?
        self.bidders = [] #who's still in the bid?
        self.bid = (None, None) #tuple of (player, bid)
        self._deal(dealer)
        self._start_bidding((dealer + 1) % len(players))

    def _deal(self, dealer):
        """Creates a deck and deals cards to each player
        """
        no_players = len(self.players)
        deck = FiveHundredDeck(no_players == 6)
        assert deck.size() == 10 * no_players + 3
        for j in [3, 4, 3]:
            for i in range(no_players):
                p = self.players[(dealer + i + 1) % no_players]
                self.player_map[p].draw(deck, j)
            self.kitty.add(deck.get_top())
        assert deck.size() == 0

    def _start_bidding(self, first_bidder):
        """Starts the bidding process.
        """
        self.state = 'bidding'
        self.bidders = list(self.players)
        self.turn = self.players[first_bidder]

    def set_bid(self, player, bid):
        """If bid is valid, set the bid to bid
        """
        #are we in bidding phase?
        if self.state != 'bidding':
            print('We\'re not in the bidding state anymore.')
            return False
        #is it the right player making the bid?
        if player != self.turn:
            print('It is not your turn to bid!')
            return False
        #is it a valid bid?
        if not valid_bid(bid):
            print('That bid is not valid')
            return False

        if bid != 'PASS':
            new_bid = Bid(bid)
            #is the bid high enough?
            if self.bid[1] is not None and self.bid[1] >= new_bid:
                print('You need to bid higher than that!')
                return False
            #cool the bid was valid so update bid
            self.bid = (player, new_bid)

        next_bidder = (self.bidders.index(self.turn) + 1) % len(self.bidders)
        self.turn = self.bidders[next_bidder]

        #did someone pass? do we have a winner?
        if bid == 'PASS':
            self.bidders.remove(player)
            if len(self.bidders) == 1:
                self.turn = self.bidders[0]
                self.player_map[self.turn].hand.extend(self.kitty)
                self.kitty.empty()
                self.state = 'kitty'
        return True

    def get_hand(self, player):
        """Returns the player's hand in a sorted order.
        """
        hand = self.player_map[player].hand
        hand_repr = []
        #sort the cards in spades, diamonds, clubs, hearts
        for s in ['S', 'D', 'C', 'H']:
            cards = list(x for x in hand if x.suit.identifier == s)
            hand_repr.extend(list(x.identifier for x in sorted(cards)))
        #add the birdie if the player has it
        if hand.has('Birdie'):
            hand_repr.append('Birdie')
        return hand_repr


class Game(object):
    """Takes a list of players. That's the order that play will be in.
    """
    def __init__(self, players):
        if len(players) != len(set(players)):
            raise SamePlayerNameException

        if len(players) != 4 and len(players) != 6:
            raise NotEnoughPlayersException

        self.players = players
        #both teams start at 0 points
        self.team_one = 0
        self.team_two = 0
        self.play = None

    def start(self):
        if self.team_one > -500 and self.team_one < 500 and \
           self.team_two > -500 and self.team_two < 500:
            self.play = Round(self.players)
