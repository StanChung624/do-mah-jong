from Player import Player
from .COMThoughtsBase import COMThoughtsBase

class Coward(COMThoughtsBase):

    def __init__(self, player: Player) -> None:
        self.bias_side = 5
        self.bias_text = 5
        super().__init__(player)

    def base_discarded_cards(self):
        return super().base_discarded_cards(5)
    
    def base_ditch_to_listen(self):
        return super().base_ditch_to_listen(1)
    
    def base_duplicate_cards(self):
        return super().base_duplicate_cards(1)
    
    def base_neighbor_cards(self):
        return super().base_neighbor_cards(1)
    
    def base_discarded_series_cards(self):
        return super().base_discarded_series_cards(1)
    
    def best_ditch(self) -> str:
        self.base_neighbor_cards()
        self.base_discarded_cards()
        self.base_duplicate_cards()
        self.base_ditch_to_listen()
        self.base_discarded_series_cards()
        return super().best_ditch()