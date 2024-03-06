from do_mah_jong.Basic import *
from do_mah_jong.Basic.CheckUtility import *
from do_mah_jong.COMStyle.COMThoughtsBase import COMThoughtsBase

test = ['l3','l4','l4','l5','l5','l6','l7','l8','l6','l9','N']

player = Player()
for card in test:
    player.draw_card(card=card)

thought = COMThoughtsBase(player)

thought.base_remove_side_straight(5)
print(thought.grades)

print(is_win(test))