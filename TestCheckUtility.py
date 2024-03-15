from do_mah_jong.Basic import *
from do_mah_jong.Basic.CheckUtility import *
from do_mah_jong.COMStyle.COMThoughtsBase import COMThoughtsBase

test = ['l1','l1','l4','l4','l5','l5','o7','o8','o9','N','N']

player = COMPlayer()
for card in test:
    player.draw_card(card=card)

player.see('o9')

player.action()