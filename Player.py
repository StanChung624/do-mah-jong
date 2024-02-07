from Deck import Deck
from CheckUtility import *

class Player():
    def __init__(self, is_owner:int=-1, index:int=0) -> None:
        self.flower = list()
        self.holding = list()
        self.is_owner = is_owner
        self.index = index

    def is_owner(self)->int:
        return self.is_owner
    
    def set_is_owner(self, is_owner:int)->None:
        self.is_owner = is_owner

    def draw_card(self, deck:Deck):
        self.holding.append(deck.serve())

    def sort_card(self):
        self.holding.sort()

    def amend_flower(self, deck:Deck):
        flag = False
        for i in range(len(self.holding)):
            card = self.holding[i]
            if 'x' in card or 'X' in card:
                self.holding.pop(i)
                self.flower.append(card)
                self.draw_card(deck)
                return self.amend_flower(deck)
        return None

    def is_win(self):        
        return is_win(self.holding)
    
    def show(self):
        self.holding.sort()
        print(self.flower)
        print(self.holding)

    def discard_card(self, card):
        if card in self.holding:
            self.holding.remove(card)
        else:
            print("Error, No card as ", card, " in holding")

    def listen(self):
        ret = list()
        for card in Deck.unique_card:
            self.holding.append(card)
            if(self.is_win()):
                ret.append(card)
            self.discard_card(card)
        return ret



if __name__ == "__main__":

    for count in range(10000):
        deck = Deck()
        stan = Player(-1)
        for i in range(16):
            stan.draw_card(deck)

        stan.amend_flower(deck)
        stan.sort_card()
        
        listen_card = stan.listen()
        if(listen_card):            
            stan.show()
            print(listen_card)
            print(1/count*100, "%")



