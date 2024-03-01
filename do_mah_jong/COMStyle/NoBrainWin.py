from do_mah_jong.Basic.Player import Player
from .COMThoughtsBase import COMThoughtsBase

class NoBrainWin(COMThoughtsBase):

    def __init__(self, player: Player) -> None:
        super().__init__(player)        

    def base_discarded_cards(self):
        return super().base_discarded_cards(0)
    
    def base_ditch_to_listen(self):
        return super().base_ditch_to_listen(5)
    
    def base_duplicate_cards(self):
        return super().base_duplicate_cards(2)
    
    def base_neighbor_cards(self):
        return super().base_neighbor_cards(2)

    def best_ditch(self) -> str:       
        self.base_neighbor_cards()
        self.base_discarded_cards()
        self.base_duplicate_cards()
        self.base_ditch_to_listen()
        return super().best_ditch()