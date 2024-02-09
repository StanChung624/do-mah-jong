from Deck import Deck
from CheckUtility import *

class Player():
    def __init__(self, holding:list=None, is_owner:int=-1, index:int=0) -> None:
        self.tracker = dict()
        for card in Deck.unique_card:
            self.tracker[card] = 4

        self.flower = list()
        if holding:
            self.holding = holding
            for card in holding:
                self.tracker[card]-=1
        else:
            self.holding = list()
        self.is_owner = is_owner
        self.index = index
        

    def is_owner(self)->int:
        return self.is_owner
    
    def set_is_owner(self, is_owner:int)->None:
        self.is_owner = is_owner

    def draw_card(self, deck:Deck):
        self.draw_card(deck.draw_card())

    def draw_card(self, card):
        self.holding.append(card)
        self.tracker[card] -=1
        

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
    
    def analyze(self):
        ret = dict()
        for card in self.holding:
            self.discard_card(card)
            listen_cards = self.listen()
            if len(listen_cards) > 0:
                ret_ = list()
                for lis in listen_cards:
                    ret_.append({lis:self.tracker[lis]})
                ret[card] = ret_
            self.holding.append(card)

        return ret



if __name__ == "__main__":

    test = ['o2', 'o3', 'o4', 'o5', 'o6', 'm5', 'm7', 'm6', 'Fa', 'Fa', 'S', 'S', 'S', 'W', 'W', 'W', 'E']

    player = Player(holding=test)

    print(player.analyze())

    # for count in range(10000):
    #     deck = Deck()
    #     stan = Player(-1)
    #     for i in range(16):
    #         stan.draw_card(deck)

    #     stan.amend_flower(deck)
    #     stan.sort_card()
        
    #     listen_card = stan.listen()
    #     if(listen_card):            
    #         stan.show()
    #         print(listen_card)
    #         print(1/count*100, "%")



