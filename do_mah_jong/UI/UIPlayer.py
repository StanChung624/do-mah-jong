from typing import Dict
from do_mah_jong.Basic.CheckUtility import Deck, Dict, List
from do_mah_jong.Basic.Deck import Deck
from do_mah_jong.Basic.Player import Player
from do_mah_jong.COMStyle.COMStyle import Normal, COMThoughtsBase
from time import sleep

class UIPlayer(Player):

    def __init__(self,
                 ui=None, 
                 holding: List[str] = None, 
                 is_owner: int = -1, 
                 index: int = 0, 
                 deck: Deck = None, 
                 seen_cards: Dict[int, List[str]] = None,
                 strategy: COMThoughtsBase = None) -> None:
        
        super().__init__(holding, is_owner, index, deck, seen_cards)
        
        if strategy is None:
            self.strategy = Normal
        else:
            self.strategy = strategy

    def copilot(self):
        if self.is_win():
            return ""
        thought = self.strategy(self)
        return thought.best_ditch()

