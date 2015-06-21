#!/usr/bin/python
from abc import ABCMeta

class Card(object):
    __metaclass__ = ABCMeta

class Pile(object):

    def __init__(self):
        self.cards = []

    def draw(self):
        """
        draw a card
        """
        pass

    def shuffle(self):
        """
        shuffle the cards
        """
        pass
