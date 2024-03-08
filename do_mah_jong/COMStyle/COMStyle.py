from do_mah_jong.Basic.Player import Player
from .COMThoughtsBase import COMThoughtsBase

class Normal(COMThoughtsBase):
    def __init__(self, player: Player) -> None:
        self.bias_side = 1
        self.bias_text = 1
        super().__init__(player)
        self.base_neighbor_cards(2)
        self.base_discarded_cards(2)
        self.base_duplicate_cards(3)
        self.base_ditch_to_listen(7)
        self.base_down_stream_player_played_cards(1)
        self.base_discarded_series_cards(1)
        self.base_remove_side_straight(5)

class PoPo(COMThoughtsBase):
    def __init__(self, player: Player) -> None:
        self.bias_side = 1
        self.bias_text = 1        
        super().__init__(player)
        self.base_neighbor_cards(1)
        self.base_discarded_cards(1)
        self.base_duplicate_cards(1)
        self.base_ditch_to_listen(1)
        self.base_down_stream_player_played_cards(5)
        self.base_discarded_series_cards(1)
        self.base_remove_side_straight(1)

class NoBrainWin(COMThoughtsBase):
    def __init__(self, player: Player) -> None:
        self.bias_side = 1
        self.bias_text = 1        
        super().__init__(player)
        self.base_neighbor_cards(2)
        self.base_discarded_cards(0)
        self.base_duplicate_cards(2)
        self.base_ditch_to_listen(5)
        self.base_down_stream_player_played_cards(1)
        self.base_discarded_series_cards(1)
        self.base_remove_side_straight(3)

class Coward(COMThoughtsBase):
    def __init__(self, player: Player) -> None:
        self.bias_side = 1
        self.bias_text = 1        
        super().__init__(player)
        self.base_neighbor_cards(1)
        self.base_discarded_cards(3)
        self.base_duplicate_cards(0.5)
        self.base_ditch_to_listen(2)
        self.base_down_stream_player_played_cards(3)
        self.base_discarded_series_cards(1)
        self.base_remove_side_straight(1)