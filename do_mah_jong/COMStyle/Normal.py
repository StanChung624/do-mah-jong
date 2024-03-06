from do_mah_jong.Basic.Player import Player
from .COMThoughtsBase import COMThoughtsBase

class Normal(COMThoughtsBase):
    def __init__(self, player: Player) -> None:
        self.bias_side = 1
        self.bias_text = 1
        super().__init__(player)
        self.base_neighbor_cards(1)
        self.base_discarded_cards(2)
        self.base_duplicate_cards(2)
        self.base_ditch_to_listen(7)
        self.base_down_stream_player_played_cards(1)
        self.base_discarded_series_cards(1)
        self.base_remove_side_straight(5)