from GameController import *

game = GameControl()

game.register_a_player(MANPlayer(is_owner= 0, index=0))
game.register_a_player(COMPlayer(is_owner=-1, index=1))
game.register_a_player(COMPlayer(is_owner=-1, index=2))
game.register_a_player(COMPlayer(is_owner=-1, index=3))

for i in range(4):
    game.register_deck(Deck())
    game.start(announce=True)
