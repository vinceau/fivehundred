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

