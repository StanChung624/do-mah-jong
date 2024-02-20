from Deck import Deck
from Player import Player

players = [Player(index=0, is_owner= 0),\
           Player(index=1, is_owner=-1),\
           Player(index=2, is_owner=-1),\
           Player(index=3, is_owner=-1)]

# serve
deck = Deck()

player_index = 0

for i in range(4):
    for j in range(4):
        players[player_index].draw_card(deck=deck)
        player_index += 1
        player_index = player_index % 4

players[0].draw_card(deck=deck)

# amend flower

for i in range(4):
    players[i].amend_flower(deck=deck)

