import sys
input = sys.stdin.readline

# I didn't use lists/dictionaries because Andrew claimed his code was faster
# So I had to outclass him and not use lists/dictionaries at all.

score = 0 # row score
cards = 0 # cards in dealing
total = 0 # complete total score

inp = input() # take in the input

# necessary outputs
print("Cards Dealt Points")
print("Clubs", end = " ") 

for a in range(len(inp)): # loop through cards
    i = inp[a]
    if i == "C": # C is the first one, don't do anything.
        continue
    # did we reach the end or a new type?
    elif i == "D" or i == "H" or i == "S" or len(inp) == a + 1:
        if cards == 2: # doubleton
            score += 1
        elif cards == 1: # singleton
            score += 2
        elif cards == 0: # void
            score = 3

        print(score) # print score

        # reset and add values
        total += score
        score = 0
        cards = 0

        # printing the card types
        if i == "D":
            print("Diamonds", end = " ")
        elif i == "H":
            print("Hearts", end = " ")
        elif i == "S":
            print("Spades", end = " ")
    # we got a card
    else:
        cards += 1 # increase amount
        if i == "A": # Ace
            score += 4
        elif i == "K": # King
            score += 3
        elif i == "Q": # Queen
            score += 2
        elif i == "J": # Joker
            score += 1
        print(i, end = " ") # print the format

print("Total", total) # print the total
