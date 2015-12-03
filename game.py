"""The game handler
"""
from lib500.fivehundred import FiveHundredDeck
from lib500.cards import Player, Pile

class Game(object):
    def __init__(self):
        self.players = [] #list of player names in the order they play
        self.player_map = {} #mapping from player names to player objects
        self.kitty = Pile()

    def add_player(self, name):
        #this is the order of play
        #player 1 and 3 are assumed to be on a team
        if name in self.players:
            print('That name is already in use!')
            return
        self.players.append(name)
        self.player_map[name] = Player(name)

    def start(self):
        no_players = len(self.players)
        if no_players != 4 and no_players != 6:
            print('You don\'t have the right number of people!')
            return
        self._deal()

    def _deal(self):
        deck = FiveHundredDeck(len(self.players) == 6)
        for i in [3, 4, 3]:
            for name in self.players:
                self.player_map[name].draw(deck, i)
            self.kitty.add(deck.get_top())

def main():
    g = Game()
    g.add_player('albert')
    g.add_player('ben')
    g.add_player('charli')
    g.add_player('derrick')
    g.start()

if __name__ == '__main__':
    main()
