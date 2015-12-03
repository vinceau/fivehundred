"""The game handler
"""
from random import shuffle
from lib500.fivehundred import FiveHundredDeck
from lib500.cards import Player, Pile

class Game(object):
    def __init__(self):
        self.players = [] #list of player names in the order they play
        self.player_map = {} #mapping from player names to player objects
        self.kitty = Pile()
        self.team_one = []
        self.team_two = []

    def add_player(self, name):
        #this is the order of play
        #player 1 and 3 are assumed to be on a team
        if name in self.players:
            print('That name is already in use!')
            return
        self.players.append(name)
        self.player_map[name] = Player(name)


    def add_team(self, team):
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
