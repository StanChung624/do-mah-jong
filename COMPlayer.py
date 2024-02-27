from typing import List
from Deck import Deck
from Player import Player
from CheckUtility import *

class COMPlayer(Player):    
    def action(self, **kwargs)->bool:
        announce = kwargs.setdefault("announce", False)
        if self.can_win:
            self.holding.append(self.saw_card)            
            return "win"
        elif self.can_eat:
            if announce:
                print("[auto] eat", end=" ")
            self.eat(formation=self.eat_formation_advisor())
            return "eat"
        elif self.can_pon:
            if announce:
                print("[auto] pon", end=" ")
            self.pon()
            return "pon"
        elif self.can_gan:
            if announce:
                print("[auto] gan", end=" ")
            self.gan()
            return "gan"
        else:
            return None

    def eat_formation_advisor(self)->List[str]:
        formations = self.eat_combinations
        if len(formations)==1:
            return formations[0]

        best_tri_count = 0
        best_formation = list()
        for formation in formations:

            holdings = self.holding + [self.saw_card]

            for card in formation:
                holdings.remove(card)

            no_txt = check_txt(holdings)[0]
            tri_count = 0
            no_use, tri_count = check_id(no_txt, "o", tri_count)
            no_use, tri_count = check_id(no_txt, "m", tri_count)
            no_use, tri_count = check_id(no_txt, "l", tri_count)

            if tri_count >= best_tri_count:
                best_tri_count = tri_count
                best_formation = formation

        return best_formation

    
    def ditch(self):
        if self.is_win():
            raise "no ditch"
        card = self.suggest_ditch()[1]
        if not card:        
            card = self.holding[0]
        return self.discard_card(card=card)

if __name__ == "__main__":
    com = COMPlayer()
    test = ['l1', 'l2', 'l3', 'm5', 'm5', 'm6', 'm7']
    for card in test:
        com.draw_card(card=card)
    print(com.listen())