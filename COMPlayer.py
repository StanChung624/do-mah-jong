from typing import List
from Deck import Deck
from Player import Player
from CheckUtility import *

class COMPlayer(Player):    
    def action(self)->bool:
        
        if self.can_win:
            self.holding.append(self.saw_card)            
            return True
        elif self.can_eat:
            # print("[auto] eat")
            self.eat(formation=self.eat_formation_advisor())
            return True
        elif self.can_pon:
            # print("[auto] pon")
            self.pon()
            return True
        elif self.can_gan:
            # print("[auto] gan")
            self.gan()
            return True
        else:
            return False

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

        return formation

    
    def ditch(self):        
        card = self.suggest_ditch()[1]
        if not card:        
            card = self.holding[0]
        return self.discard_card(card=card)

if __name__ == "__main__":
    com = COMPlayer()
    test = ["l3","l3","l4","l5","l6","l7","l8"]
    for card in test:
        com.draw_card(card=card)
    com.see("l6")

    print(com.eat_formation_advisor())