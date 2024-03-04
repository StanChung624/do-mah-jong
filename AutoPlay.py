from do_mah_jong.Basic import *
from do_mah_jong.COMStyle.PoPo import PoPo

game = GameControl()

game.register_a_player(MANPlayer(is_owner= 0, index=0))
game.register_a_player(COMPlayer(is_owner=-1, index=1))
game.register_a_player(COMPlayer(is_owner=-1, index=2))
game.register_a_player(COMPlayer(is_owner=-1, index=3, strategy=PoPo))

for i in range(1):
    game.register_deck(Deck())
    game.start(announce=True)
    print(game.game_report.records[-1])
