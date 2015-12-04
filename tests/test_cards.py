from fivehundred.cards import PlayingCard, suits, values

def test_equal_playing_cards():
    c1 = PlayingCard(suits['hearts'], values['2'])
    c2 = PlayingCard(suits['hearts'], values['3'])
    assert(c1 < c2)
