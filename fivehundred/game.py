"""The game handler
"""
from random import shuffle
from fivehundred.core import FiveHundredDeck
from fivehundred.bids import valid_bid, bid_value, Bid
from fivehundred.cards import Player, Pile

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

class Game(object):
    def __init__(self):
        self.players = [] #list of player names in the order they play
        self.player_map = {} #mapping from player names to player objects
        self.kitty = Pile()
        self.team_one = []
        self.team_two = []
        self.dealer = 0
        self.bidders = []
        self.state = 'initialised'
        self.current_bidder = 0
        self.winning_bid = None
        self.trumpsuit = None

    def add_player(self, name):
        if not self.state == 'initialised':
            return self._wrong_state()
        #this is the order of play
        #player 1 and 3 are assumed to be on a team
        if name in self.players:
            print('That name is already in use!')
            return
        self.players.append(name)
        self.player_map[name] = Player(name)


    def add_team(self, team):
        if not self.state == 'initialised':
            return self._wrong_state()
        team_size = len(team)
        #ensure teams are of the right size
        if team_size != 2 and team_size != 3:
            print('Teams must be of two or three!')
            return
        #ensure players have unique names
        name_used = any(name in self.players for name in team)
        if len(team) != len(set(team)) or name_used:
            print('Players need to have different names!')
            return
        #handle first team
        if not self.team_one:
            #add first team
            self.team_one = team
            for n in team:
                self.player_map[n] = Player(n)
            return
        #handle second team
        if team_size != len(self.team_one):
            print('The two teams need to be of the same size!')
            return
        #teams are of the same size
        self.team_two = team
        #randomise the order
        shuffle(self.team_one)
        shuffle(self.team_two)
        for i in range(team_size):
            self.players.append(self.team_one[i])
            self.players.append(self.team_two[i])

    def start(self):
        no_players = len(self.players)
        if no_players != 4 and no_players != 6:
            print('You don\'t have the right number of people!')
            return
        self._deal()
        self._bidding()

    def _deal(self):
        deck = FiveHundredDeck(len(self.players) == 6)
        for i in [3, 4, 3]:
            for name in self.players:
                self.player_map[name].draw(deck, i)
            self.kitty.add(deck.get_top())

    def _bidding(self):
        """Start the bidding process
        """
        bid_order = Order(self.players, self.dealer + 1)
        self.bidders = list(bid_order)
        self.state = 'bidding'

    def set_bid(self, player, bid):
        #are we in bidding phase?
        if self.state != 'bidding':
            return self._wrong_state()
        #is it the right player making the bid?
        if player != self.bidders[self.current_bidder]:
            print('It is not your turn to bid!')
            return False
        #is it a valid bid?
        if not valid_bid(bid):
            print('That bid is not valid')
            return False
        new_bid = Bid(bid)
        #did someone pass? do we have a winner?
        if bid == 'PASS':
            del self.bidders[self.current_bidder]
            if len(self.bidders) == 1:
                #wooh! finally done
                #distribute kitty
                self.trumpsuit = self.winning_bid.suit
                self.bidders[0].hand.extend(self.kitty)
                self.kitty.empty()
                self.state = 'kitty'
                return True
        #is the bid high enough?
        elif self.winning_bid >= new_bid:
            print('You need to bid higher than that!')
            return False
        #yep valid bid
        else:
            self.current_bidder += 1
            self.winning_bid = new_bid
        #rewrap bidder if necessary
        if self.current_bidder > len(self.players):
            self.current_bidder = 0 #back to start
        return True

    def drop(self, cards):
        if self.state != 'kitty':
            return self._wrong_state()

    def _wrong_state(self):
        print('There\'s a time and place for everything.')
        return False

    def _reset(self):
        #next person deals
        self.dealer += 1
        self.kitty.empty() #this is important


def main():
    g = Game()
    g.add_player('albert')
    g.add_player('ben')
    g.add_player('charli')
    g.add_player('derrick')
    g.start()

if __name__ == '__main__':
    main()
