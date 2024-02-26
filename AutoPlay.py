from Deck import Deck
from MANPlayer import MANPlayer
from COMPlayer import COMPlayer

deck = Deck()

players = [COMPlayer(index=0, is_owner= 0, deck=deck),
           COMPlayer(index=1, is_owner=-1, deck=deck),
           COMPlayer(index=2, is_owner=-1, deck=deck),
           COMPlayer(index=3, is_owner=-1, deck=deck)]

for i in range(4):
    for id in range(4):        
        for j in range(4):
            players[id].draw_card(announce=False) 


# amend flower
for i in range(4):
    players[i].amend_flower()

id = 0

round = 0

to_stop = False
while not to_stop:

    if id==0:
        round += 1

    if not players[id].draw_card():
        print("no body win..")
        to_stop = True
        break

    players[id].amend_flower()

    if players[id].is_win():
        is_stop = True
        print("win!")
        players[id].show()
        break

    card = players[id].ditch()

    def others_check(card, current_player_id)->int:
        print("player", current_player_id, "ditch", card)
        other_ids = [0,1,2,3]
        other_ids.remove(current_player_id)

        for other in other_ids:
            players[other].see(card=card, player=players[current_player_id])
        
        other_ids.reverse()
        for other in other_ids:
            if players[other].action(announce=True):
                print("Player", other)

                if players[other].is_win():
                    print("win!")
                    players[other].show()                    
                    return None
                
                current_player_id = other
                return others_check(players[other].ditch(), current_player_id)
                
        return current_player_id

    id = others_check(card, id)    
    if id is None:
        break
    
    id += 1
    id %= 4

print("round", round)