from do_mah_jong.Basic.Player import Player
from .COMThoughtsBase import COMThoughtsBase

class Normal(COMThoughtsBase):
    def __init__(self, player: Player) -> None:
        self.bias_side = 1
        self.bias_text = 1
        super().__init__(player)
        self.base_neighbor_cards()
        self.base_discarded_cards()
        self.base_duplicate_cards()
        self.base_ditch_to_listen()
        self.base_down_stream_player_played_cards()        
        self.base_discarded_series_cards()

    def base_discarded_cards(self):
        return super().base_discarded_cards(1)
    
    def base_ditch_to_listen(self):
        return super().base_ditch_to_listen(5)
    
    def base_duplicate_cards(self):
        return super().base_duplicate_cards(2)
    
    def base_neighbor_cards(self):
        return super().base_neighbor_cards(2)
    
    def base_down_stream_player_played_cards(self):
        return super().base_down_stream_player_played_cards(1)
    
    def base_discarded_series_cards(self):
        return super().base_discarded_series_cards(1)

    def best_ditch(self) -> str:
        return super().best_ditch()