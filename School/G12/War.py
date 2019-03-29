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

    def amount(self):
        """return the amount of cards in a deck"""
        return len(self.cards)

# Create the center deck of all cards.
deck = Deck()
for a in ranks:
    for b in suits:
        deck.add_card(Card(b, a))

deck.shuffle() # shuffle the deck

# Start sending cards to each deck.
D1 = Deck()
D2 = Deck()
you = False
for card in deck.cards:
    you = not you
    if you: # pass to each user
        D1.add_card(card)
    else:
        D2.add_card(card)
deck.cards = [] # empty center

print("----------------------------------------------")
print("WELCOME TO WAR                 MADE BY MAKAN D")
print("----------------------------------------------")

rnd = 1
war = False
D1_owned = Deck()
D2_owned = Deck()
print("[GAME] Currently on round: 1")
while 1:
    center = []
    choice = input("$ ")
    if choice == "amount":
        print("Your Holding Hand:", D1.amount(), "- Deck:", D1_owned.amount())
    elif choice == "opp amount":
        print("Opponent Holding Hand:", D2.amount(), "- Deck:", D2_owned.amount())
    elif choice == "draw":
        if not war: # no war
            center.append(D1.deal_one()) # deal from you
            center.append(D2.deal_one()) # deal from opponent

            # both deal comparison cards
            c1 = D1.deal_one()
            c2 = D2.deal_one()

            # comapre the ranks
            rank = c1.compare(c2)
            if rank == -1: # lost
                print("[LOST] Your", c1, "got destroyed by", c2)
            elif rank == 0:
                print("[WAR] You're at war with", c1, "and", c2)
            else:
                 print("[WON] Your", c1, "destroyed", c2)
