from Deck import Deck
from Player import Player

class CoPlayer(Player):    
    def action(self)->bool:
        
        if self.can_eat:
            print("[auto] eat")
            self.eat(formation=self.eat_combinations[0])
            return True
        elif self.can_pon:
            print("[auto] pon")
            self.pon()
            return True
        elif self.can_gan:
            print("[auto] gan")
            self.gan()
            return True
        elif self.can_win:
            self.show()            
            return True
        else:
            return False

    def ditch(self):
        card = self.grade()[1]
        if not card:        
            card = self.holding[0]
        return self.discard_card(card=card)

if __name__ == "__main__":
    deck = Deck()
    cop = CoPlayer(deck=deck)

    for i in range(16):
        cop.draw_card()

    cop.amend_flower()

    to_stop = False
    while not to_stop:

        card = deck.serve()

        if not card:
            to_stop = True
            break

        cop.draw_card(card=card)
        print("draw:", card)        

        cop.amend_flower()

        cop.ditch()
        cop.show()
        
        for i in range(3):

            card = deck.serve()
            if not card:
                to_stop = True
                break

            while "x" in card or "X" in card:
                card = deck.serve()
                if not card:
                    to_stop = True
                    
            if not to_stop:

                cop.see(card=card)
                print("see:", card)
                if cop.action():
                    if cop.is_win():
                        cop.show()  
                        to_stop = False                
                        
                    cop.ditch()
                    cop.show()

