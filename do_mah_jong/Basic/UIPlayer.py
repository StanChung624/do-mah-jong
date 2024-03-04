from typing import Dict
from do_mah_jong.Basic.CheckUtility import Deck, Dict, List
from do_mah_jong.Basic.Deck import Deck
from do_mah_jong.Basic.Player import Player
from time import sleep

class UIPlayer(Player):

    def __init__(self, ui=None, holding: List[str] = None, is_owner: int = -1, index: int = 0, deck: Deck = None, seen_cards: Dict[int, List[str]] = None) -> None:
        

        super().__init__(holding, is_owner, index, deck, seen_cards)

    def __action_interface(self)->bool:
        msg = ""
        actions = []
        opt = 1
        if(self.can_eat):
            msg += str(opt) + " eat\n"
            actions.append(self.eat)
            opt+=1
        if(self.can_pon):
            msg += str(opt) + " pon\n"
            actions.append(self.pon)
            opt+=1
        if(self.can_gan):
            msg += str(opt) + " gan\n"
            actions.append(self.gan)
            opt+=1
        if(self.can_win):
            msg += str(opt) + " win\n"
            self.holding.append(self.see_card)            
            actions.append(self.show)
            opt+=1

        if self.can_eat or self.can_gan or self.can_pon or self.can_win:            
            self.show()
            print("actions:")
            print(msg, "0 none")
            opt = int(input())-1
            if opt >= 0:
                actions[opt]()
                return actions[opt].__name__
            else:
                return None                
            
        else:
            return None

    def action(self, **kwargs)->bool:
        return self.__action_interface()
    
    @Player._sort
    def show_holdings(self):
        btn = 0
        for card in self.holding:
            self.tiles[btn].setText(card)
            def btn_func():
                self.ui_ditch_card = card
                print(card)
                return None
            self.tiles[btn].clicked.connect(btn_func)
            btn += 1
        btn = 0
        for card in self.flower:
            self.flws[btn].setText(card)
    
    def ditch(self) -> str:
        self.show_holdings()
        self.ui_ditch_card = None
        for i in range(5):            
            sleep(1)
        return self.__discard_card_interface()

    def __discard_card_interface(self):        
        card = self.ui_ditch_card
        return self.discard_card(card=card)