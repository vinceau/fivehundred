from fivehundred.cards import *

def test_compare_playing_cards():
    c1 = PlayingCard(suits['hearts'], values['2'])
    c2 = PlayingCard(suits['hearts'], values['3'])
    assert(c1 < c2)
    c3 = PlayingCard(suits['hearts'], values['3'])
    assert(c2 == c3)
    c4 = PlayingCard(suits['diamonds'], values['3'])
    assert(c3 == c4)

def test_pile():
    p = Pile()
    assert p.size() == 0
    p.add(Card('a'))
    assert p.size() == 1
    p.add(Card('b'))
    assert p.size() == 2
    assert p.get_top().identifier == 'b'
    assert p.size() == 1
