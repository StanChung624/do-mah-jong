from Deck import Deck
from Player import Player

deck = Deck()

players = list([Player(0,0), Player(-1,1), Player(-1,2), Player(-1,3)])

# deal all cards
for i in range(65):
    players[i%4].draw_card(deck)

# amend for flower cards
for i in range(4):
    players[i].amend_flower(deck)

for i in range(4):
    print("Player #", i, ":")
    players[i].show()