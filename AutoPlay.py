from Deck import Deck
from Player import Player
from CoPlayer import CoPlayer


deck = Deck()

players = [Player(index=0, is_owner= 0, deck=deck),\
           CoPlayer(index=1, is_owner=-1, deck=deck),\
           CoPlayer(index=2, is_owner=-1, deck=deck),\
           CoPlayer(index=3, is_owner=-1, deck=deck)]

for i in range(4):
    for id in range(4):        
        for j in range(4):
            players[id].draw_card() 


# amend flower
for i in range(4):
    players[i].amend_flower()

id = 0

to_stop = False
while not to_stop:

    players[id].draw_card()
    players[id].amend_flower()

    if players[id].is_win():
        is_stop = True
        print("win!")

    card = players[id].ditch()

    print("Player", id, "ditch", card)

    other_ids = [0,1,2,3]
    other_ids.remove(id)

    for other in other_ids:
        players[other].see(card=card, player=players[id])
    
    other_ids.reverse()
    for other in other_ids:
        if players[other].action():
            if players[other].is_win():
                is_stop = True
                print("win!")
            print("Player", other)
            print("\t ditch:", players[other].ditch())
            id = other
            break

    id += 1
    id %= 4
