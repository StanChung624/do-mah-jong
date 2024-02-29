from GameController import *
from COMThoughts import Coward

game = GameControl()

game.register_a_player(COMPlayer(is_owner= 0, index=0, strategy=Coward))
game.register_a_player(COMPlayer(is_owner=-1, index=1))
game.register_a_player(COMPlayer(is_owner=-1, index=2))
game.register_a_player(COMPlayer(is_owner=-1, index=3))

for i in range(20):
    game.register_deck(Deck())
    game.start()
    print(game.game_report.records[-1])
