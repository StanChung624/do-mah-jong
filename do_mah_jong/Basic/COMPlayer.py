from typing import Dict, List
from do_mah_jong.Basic.CheckUtility import Dict
from do_mah_jong.Basic.Deck import Deck
from do_mah_jong.Basic.Player import Player
from do_mah_jong.Basic.CheckUtility import *
from do_mah_jong.COMStyle.COMThoughtsBase import COMThoughtsBase 
from do_mah_jong.COMStyle.COMStyle import *

class COMPlayer(Player):    

    def __init__(self, 
                 strategy:COMThoughtsBase = None,
                 holding: List[str] = None, 
                 is_owner: int = -1, 
                 index: int = 0, 
                 deck: Deck = None, 
                 seen_cards: Dict[int, List[str]] = None) -> None:
        if strategy is None:
            self.strategy = NoBrainWin
        else:
            self.strategy = strategy

        super().__init__(holding, is_owner, index, deck, seen_cards)

    def action(self, **kwargs)->bool:
        announce = kwargs.setdefault("announce", False)
        if self.can_win:
            self.win()
            return "win"
        elif self.can_eat:

            formation=self.eat_formation_advisor()
            should_eat = self.should_eat_check(formation=formation)

            if should_eat:
                if announce:
                    print("[auto] eat", end=" ")
                self.eat(formation=formation)
                return "eat"
            else:
                return None
        elif self.can_gan:
            if announce:
                print("[auto] gan", end=" ")
            self.gan()
            return "gan"
        elif self.can_pon:
            if announce:
                print("[auto] pon", end=" ")
            self.pon()
            return "pon"
        else:
            return None

    def eat_formation_advisor(self)->List[str]:
        formations = self.eat_combinations
        if len(formations)==1:
            return formations[0]

        best_in_count = 0
        best_formation = formations[0]
        for formation in formations:

            holdings = self.holding + [self.see_card]

            holdings.sort()

            for card in formation:
                holdings.remove(card)

            in_count = len(listen(holdings, True))

            if in_count > best_in_count:
                best_in_count = in_count
                best_formation = formation

        return best_formation

    def should_eat_check(self, formation=List[str]):
        holding = list(self.holding)
        holding.remove(formation[0])
        holding.remove(formation[2])
        if self.strategy(self, holding=holding).best_ditch() == self.see_card:
            return False
        else:
            return True

    @Player._sort
    def suggest_ditch(self)->str:
        thoughts = self.strategy(self)
        return thoughts.best_ditch()
    
    def ditch(self):
        if self.is_win():
            raise "no ditch"
        card = self.suggest_ditch()
        if not card:        
            card = self.holding[0]
        return self.discard_card(card=card)

if __name__ == "__main__":
    com = COMPlayer(deck=Deck())
    
    test = ['l1', 'l2', 'l3', 'l4', 'l5']
    for card in test:
        com.draw_card(card=card)

    com.see("l3", player_index=1)

    print(com.eat_combinations)

    print(com.eat_formation_advisor())