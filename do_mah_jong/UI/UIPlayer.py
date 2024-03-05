from typing import Dict
from do_mah_jong.Basic.CheckUtility import Deck, Dict, List
from do_mah_jong.Basic.Deck import Deck
from do_mah_jong.Basic.Player import Player
from do_mah_jong.COMStyle.Normal import Normal, COMThoughtsBase
from time import sleep

class UIPlayer(Player):

    def __init__(self,
                 ui=None, 
                 holding: List[str] = None, 
                 is_owner: int = -1, 
                 index: int = 0, 
                 deck: Deck = None, 
                 seen_cards: Dict[int, List[str]] = None,
                 copilot_type: COMThoughtsBase = None) -> None:
        
        super().__init__(holding, is_owner, index, deck, seen_cards)
        
        if copilot_type is None:
            self.copilot_type = Normal
        else:
            self.copilot_type = copilot_type

    def copilot(self):
        if self.is_win():
            return ""
        thought = self.copilot_type(self)
        print(thought.grades)
        return thought.best_ditch()

