import random

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'hearts', 'clubs', 'diamonds']

class Card():
    """class for a specific card"""

    def __init__(self, suit, rank):
        """start a new card (suit, rank)"""
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        """return the suit and rank of a card"""
        return "%s %s" % (self.suit, self.rank)

    def compare(self, alternate):
        """compare the rank of two cards together"""
        me_rank = ranks.index(self.rank)
        alternate_rank = ranks.index(alternate.rank)

        if me_rank == alternate_rank:
            return 0
        elif me_rank < alternate_rank:
            return -1
        else:
            return 1

class Deck():
    """class for deck of card objects"""

    def __init__(self):
        """start the deck bro"""
        self.cards = []

    def add_card(self, card):
        """a card to the top of the deck"""
        self.cards.append(card)

    def shuffle(self):
        """shuffle the deck of cards"""
        random.shuffle(self.cards)

    def deal_one(self):
        """deal a card from the top of the deck"""
        return self.cards.pop(-1)

# CREATE A DECK OF CARDS
# -----------------------

deck = Deck()
for a in ranks:
    for b in suits:
        t_ = Card(b, a)
        deck.add_card(t_)
