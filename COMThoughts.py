from COMThoughtsBase import COMThoughtsBase
from Player import Player

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

    def best_ditch(self) -> str:
        self.base_neighbor_cards()
        self.base_discarded_cards()
        self.base_duplicate_cards()
        self.base_ditch_to_listen()        
        return super().best_ditch()
    
class PoPo(COMThoughtsBase):

    def __init__(self, player: Player) -> None:
        self.bias_side = 0
        self.bias_text = 0
        super().__init__(player)

    def base_discarded_cards(self):
        return super().base_discarded_cards(1)
    
    def base_ditch_to_listen(self):
        return super().base_ditch_to_listen(1)
    
    def base_duplicate_cards(self):
        return super().base_duplicate_cards(1)
    
    def base_neighbor_cards(self):
        return super().base_neighbor_cards(1)
    
    def base_down_stream_player_palyed_cards(self):
        return super().base_down_stream_player_palyed_cards(5)

    def best_ditch(self) -> str:
        self.base_neighbor_cards()
        self.base_discarded_cards()
        self.base_duplicate_cards()
        self.base_ditch_to_listen()
        self.base_down_stream_player_palyed_cards()        
        return super().best_ditch()

if __name__ == "__main__":
    deck = ['l1', 'l2', 'l3', 'm5', 'm5', 'm6', 'm7', 'N']
    player = Player(holding=deck, index=0)

    player.see("l1", player_index=1)
    player.see("l2", player_index=2)
    player.see("l3", player_index=3)

    thought = PoPo(player)
    
    print(thought.best_ditch())
    print(thought.grades)
