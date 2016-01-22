
from fivehundred.game import Game, NotEnoughPlayersException
from fivehundred.bids import Bid

def test_game_start():
    try:
        g = Game(['a', 'b'])
        assert False
    except NotEnoughPlayersException:
        assert True
    try:
        g = Game(['a', 'b', 'c', 'd'])
        assert True
    except NotEnoughPlayersException:
        assert False
    g.start()
    assert g.play is not None
    assert g.play.turn == 'b'
    #player a dealt so shouldn't be able to bid
    assert not g.play.set_bid('a', 'asdfasdf')
    assert not g.play.set_bid('a', '6X')
    assert not g.play.set_bid('b', 'asdfasdf')
    #player b bids
    assert g.play.set_bid('b', '6S')
    assert g.play.bid == ('b', Bid('6S'))
    #next bidder should be c
    assert g.play.turn == 'c'
    #player b can't bid anymore
    assert not g.play.set_bid('b', '6C')
    assert g.play.set_bid('c', '6C')
    assert g.play.bid == ('c', Bid('6C'))
    assert g.play.turn != 'c'
    assert g.play.turn == 'd'
    assert g.play.set_bid('d', 'PASS')
    assert g.play.turn == 'a'
    assert g.play.set_bid('a', 'PASS')
    assert g.play.turn == 'b'
    assert g.play.set_bid('b', '7S')
    assert g.play.turn == 'c'
    assert g.play.set_bid('c', 'PASS')
    assert g.play.turn == 'b'
    #we can't bid any cuz it's not in bidding phase
    assert not g.play.set_bid('b', 'PASS')
    assert g.play.state == 'kitty'
